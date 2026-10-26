# Emergence-assets

Shared assets for the [Emergence](https://github.com/charlie-yus/Emergence) thesis workflow: AI skills mapped to each route and step, a LaTeX thesis template, Word layout rules and tools, and small checking scripts.

- Skills are organized by research route (secondary-data empirical, survey empirical, survey diagnosis and strategy, case study) and by workflow step.
- Third-party skills are included unmodified under their original licenses (Apache-2.0 / MIT); see `skills/README.md`.
- Documentation is in Chinese.

---

## 中文说明

这里放 Emergence 论文工作流共用的素材。**你的 AI 按 Emergence 的 `AGENTS.md` 走到对应步骤时，会自己来这里找。**

| 位置 | 内容 | 什么时候用 |
|---|---|---|
| `skills/` | 给 AI 的 Skills，`skills/README.md` 列出哪一步、哪条路线用哪个 | 每一步开始前查一下对照表 |
| `skills/wuhan-college-thesis-latex/` | 学校文经管类本科论文 LaTeX 模板（也是一个 Skill）：`assets/template/` 里是可直接编译的示例，`references/` 里是规范与取值依据 | 第 12 步，选 LaTeX 排版时 |
| `word-tools/` | Word 版面规则和留白修复脚本 | 第 12 步，选 Word 排版时 |
| `tools/check_numbers.py` | 数字核对：正文里每个带小数的数字，都要能在结果表（CSV）里找到 | 第 9、13、16 步，实证路线 |

## 用 LaTeX 模板

需要 XeLaTeX（TeX Live 或 MacTeX）。

```bash
python3 skills/wuhan-college-thesis-latex/scripts/new_project.py /绝对路径/我的论文
python3 skills/wuhan-college-thesis-latex/scripts/build.py /绝对路径/我的论文/main.tex --out /绝对路径/我的论文/build
```

- 字体：`local-fonts.tex` 默认对应 Mac 自带字体。Windows 上装有宋体、黑体、仿宋、楷体时，用 `\documentclass[strictfonts]{whcthesis}`。**本仓库不附带字体文件。**
- 封面信息填在 `main.tex` 的 `\WhcSetup{...}` 里；完成时间、签名、致谢不要让 AI 编。
- 详细接口见 `skills/wuhan-college-thesis-latex/references/usage.md`。

## 用数字核对脚本

```bash
python3 tools/check_numbers.py 草稿.md 结果目录
```

结果目录下的所有 CSV 都算“结果表”。找不到的数字会逐个列出，需要人工确认它从哪来。

## 不在这里的东西

- “常用控制变量”包（数据库数据，不能公开）：问 Charlie 要。
- 商用字体：自己安装。
- 学校格式原件：在 Emergence 的 `resources/school-format-original.doc`。

## 维护

改完这里的内容后，在 Emergence 的 `CHANGELOG.md` 加一条说明，组员的 AI 才会注意到。
