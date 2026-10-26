# -*- coding: utf-8 -*-
"""数字核对：草稿里每个带小数的数字，都必须能在结果 CSV 里找到（按 1—4 位四舍五入或百分数匹配）。
用法：python3 check_numbers.py 草稿.md 结果目录（目录下所有 CSV 的数值都算“结果表”）。
排除：$…$ 公式；草稿里“## 表号对照”之后的内容。找不到的数字逐个列出，需人工确认来源。"""
import glob, re, sys
from pathlib import Path
import pandas as pd

if len(sys.argv) < 3:
    sys.exit(__doc__)
draft, res = Path(sys.argv[1]), Path(sys.argv[2])
vals = set()
for f in glob.glob(str(res / "**/*.csv"), recursive=True):
    try:
        d = pd.read_csv(f)
    except Exception:
        continue
    for c in d.columns:
        if pd.api.types.is_numeric_dtype(d[c]):
            for v in d[c].dropna().values:
                for k in (1, 2, 3, 4):
                    vals.add(round(float(v), k)); vals.add(round(float(v) * 100, k))
s = draft.read_text(encoding="utf-8").split("## 表号对照")[0]
s = re.sub(r"\$[^$]*\$", "", s)
nums = re.findall(r"(?<![\d.])-?\d+\.\d{1,3}(?!\d)", s)
miss = sorted({n for n in nums if float(n) not in vals and -float(n) not in vals})
print(f"带小数的数字 {len(nums)} 个；结果表中找不到 {len(miss)} 个")
for n in miss:
    i = s.find(n)
    print(" ", n, "｜", s[max(0, i - 30):i + 10].replace("\n", " "))
sys.exit(1 if miss else 0)
