# -*- coding: utf-8 -*-
"""留白修复：渲染 PDF → 找出底部留白超过 1/4 的页 → 若下一页开头是图或表，
把该图（表）块后面紧跟的一段正文移到图（表）块之前，让正文先填满当前页；图（表）仍在引用它的段落之后，只是往后推一段。
规则：不跨标题、不越过下一张图或表、每块最多后移 4 段；重复渲染直到没有可修的页。
用法：python3 fix_layout.py 输入.docx 输出目录"""
import re, subprocess, sys, shutil, json, os
from pathlib import Path
import fitz
from docx import Document
from docx.oxml.ns import qn

src, out = Path(sys.argv[1]), Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)
work = out / src.name
shutil.copy(src, work)
TOP, BOTTOM = 30 / 25.4 * 72, 842 - 25 / 25.4 * 72          # 版心上下边界（pt）
EXEMPT_NEXT = ("摘", "Abstract", "目", "参考文献", "致", "附", "引")    # 下一页以这些开头时，本页为规定另起页之前，不算


def render(docx):
    # LibreOffice：默认用 PATH 里的 soffice，可用环境变量 SOFFICE 指定；同目录有 fonts.conf 时用它找中文字体
    fc = Path(__file__).resolve().parent / "fonts.conf"
    env = {**os.environ, **({"FONTCONFIG_FILE": str(fc)} if fc.exists() else {})}
    subprocess.run([os.environ.get("SOFFICE") or shutil.which("soffice") or "soffice", "--headless", "--convert-to", "pdf", "--outdir", str(out), str(docx)], check=True, capture_output=True, env=env)
    return out / (docx.stem + ".pdf")


def page_info(pdf):
    d = fitz.open(pdf)
    info = []
    for i, p in enumerate(d):
        lines = []
        for b in p.get_text("dict")["blocks"]:
            for ln in b.get("lines", []):
                t = "".join(s["text"] for s in ln["spans"]).strip()
                if t and TOP - 5 < ln["bbox"][1] < BOTTOM - 2:
                    lines.append((ln["bbox"][1], ln["bbox"][3], t))
        imgs = [im["bbox"] for im in p.get_image_info() if TOP - 5 < im["bbox"][1] < BOTTOM]
        ys = [l[1] for l in lines] + [b[3] for b in imgs]
        bottom = max(ys) if ys else TOP
        firsts = sorted([(l[0], l[2]) for l in lines] + [(b[1], "[图片]") for b in imgs])
        info.append({"page": i + 1, "gap": (BOTTOM - bottom) / (BOTTOM - TOP), "first": [t for _, t in firsts[:4]], "text": [l[2] for l in lines],
                     "img_h": (min(imgs, key=lambda b: b[1])[3] - min(imgs, key=lambda b: b[1])[1]) if imgs else 0})
    return info


def is_heading(el):
    st = el.find(qn("w:pPr") + "/" + qn("w:pStyle"))
    return st is not None and st.get(qn("w:val"), "").startswith(("Heading", "TOC"))


def txt(el):
    return "".join(el.itertext()).strip()


def block_of(doc, label):
    """按图号（“图N”）或表号（“表N”）找到块：图＝图片段＋图题＋注；表＝（空隔段）＋表格＋注。返回块元素列表。"""
    body = list(doc.element.body)
    for k, el in enumerate(body):
        if label.startswith("图") and el.tag == qn("w:p") and re.match(label + r"\s", txt(el)) and k > 0 and body[k - 1].findall(".//" + qn("w:drawing")):
            blk = [body[k - 1], el]
            j = k + 1
            while j < len(body) and body[j].tag == qn("w:p") and txt(body[j]).startswith(("注：", "资料来源：")):
                blk.append(body[j]); j += 1
            return blk
        if label.startswith("表") and el.tag == qn("w:tbl") and re.match(label + r"\s", txt(el.find(".//" + qn("w:tc")))):
            blk = [el]
            j = k + 1
            while j < len(body) and body[j].tag == qn("w:p") and txt(body[j]).startswith(("注：", "资料来源：")):
                blk.append(body[j]); j += 1
            return blk
    return None


def movable_after(blk):
    nxt = blk[-1].getnext()
    if nxt is None or nxt.tag != qn("w:p") or is_heading(nxt) or nxt.findall(".//" + qn("w:drawing")) or nxt.findall(".//" + qn("w:sectPr")):
        return None
    t = txt(nxt)
    if not t or t.startswith(("注：", "资料来源：", "图", "表")):
        return None
    # 移走后最多允许两张图相连（每张图仍在引用它的段落之后），不得出现三张图连排
    def is_fig(el):
        return el is not None and el.tag == qn("w:p") and el.findall(".//" + qn("w:drawing"))
    def fig_end(el):                         # 图片段 → 图题 → 注／资料来源，返回块末元素
        e = el.getnext()
        while e is not None and e.tag == qn("w:p") and (txt(e).startswith(("注：", "资料来源：")) or re.match(r"^图\d+\s", txt(e))):
            el, e = e, e.getnext()
        return el
    prev = blk[0].getprevious()
    prev_is_fig = prev is not None and prev.tag == qn("w:p") and txt(prev).startswith(("注：", "资料来源：", "图"))
    after = nxt.getnext()
    if after is None or after.tag != qn("w:p") or is_heading(after):
        return None
    if is_fig(after):
        if prev_is_fig:
            return None
        end2 = fig_end(after).getnext()
        if is_fig(end2):
            return None
    elif not txt(after) or txt(after).startswith(("注：", "资料来源：")):
        return None
    return nxt


def shrink(blk, scale):
    for ext in blk[0].iter():
        if ext.tag.endswith("}extent") or ext.tag.endswith("}ext"):
            if ext.get("cx"):
                ext.set("cx", str(int(int(ext.get("cx")) * scale))); ext.set("cy", str(int(int(ext.get("cy")) * scale)))


moves, history, shrunk = {}, [], {}
for it in range(25):
    pdf = render(work)
    info = page_info(pdf)
    bad = []
    for a, b in zip(info, info[1:]):
        if a["gap"] <= 0.25 or any(b["first"] and b["first"][0].startswith(x) for x in EXEMPT_NEXT):
            continue
        lab = None
        for t in b["first"][:3]:
            m = re.match(r"^(图\d+|表\d+)\s", t)
            if m:
                lab = m.group(1); break
        if lab is None and b["first"] and b["first"][0] == "[图片]":
            for t in b["text"][:30]:
                m = re.match(r"^(图\d+)\s", t)
                if m:
                    lab = m.group(1); break
        bad.append((a["page"], round(a["gap"], 3), lab))
    history.append({"iteration": it, "pages": len(info), "bad": bad})
    doc = Document(work)
    changed = False
    for page, gap, lab in bad:
        if not lab or moves.get(lab, 0) >= 4:
            continue
        blk = block_of(doc, lab)
        if not blk:
            continue
        para = movable_after(blk)
        if para is not None:
            blk[0].addprevious(para)
            moves[lab] = moves.get(lab, 0) + 1
            changed = True
            break                           # 每轮只动一处，避免连锁误判
        if lab.startswith("图") and lab not in shrunk:
            nxt_page = info[page]               # 下一页（page 为 1 起，故下标即下一页）
            avail = gap * (BOTTOM - TOP) - 70   # 图题、注约 70pt
            h = nxt_page["img_h"]
            if h and 0.8 <= avail / h < 1:
                shrink(blk, avail / h - 0.01)
                shrunk[lab] = round(avail / h - 0.01, 3)
                changed = True
                break
    if not changed:
        break
    doc.save(work)

final = page_info(render(work))
report = {"moves": moves, "shrunk": shrunk, "history": history,
          "remaining_gaps": [(p["page"], round(p["gap"], 3)) for p, q in zip(final, final[1:]) if p["gap"] > 0.25 and not any(q["first"] and q["first"][0].startswith(x) for x in EXEMPT_NEXT)],
          "pages": len(final)}
(out / "留白修复记录.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps({k: report[k] for k in ("moves", "shrunk", "remaining_gaps", "pages")}, ensure_ascii=False))
