---
name: wuhan-college-thesis-latex
description: Use when creating, repairing, or applying a Wuhan College undergraduate thesis LaTeX layout in humanities, economics, or management (武汉学院文经管类本科毕业论文), including school-format covers, tables, equations, contents, and page numbering. For defense slides use the separate Beamer skill.
---

# 武汉学院文经管论文 LaTeX

以学校文经管成品示例为依据，在新项目中排版。学校模板原件保存在 `assets/school-reference.doc`，出处和SHA见 `references/source.json`；先读 `references/format-decisions.md`、`references/usage.md`；输出 Word 时还要读 `references/word-layout-rules.md`。原件另含理工类，不可混用。

## 开始

运行 `python3 scripts/new_project.py /绝对路径/新目录`，目标必须不存在。将用户确认的元数据填入 `main.tex` 的 `\WhcSetup`；空日期、签名、致谢不自动编造。把正文导入新项目，保留原字句、引用、数据及图像，不在套版过程中改研究结论、排序文献或应用新的回归数字。

默认 `local-fonts.tex` 是本机已标定的 Apple 字体映射，不等于微软宋体。其他机器先配置字体路径；有学校指定的 Windows 字体可用 `strictfonts`，仍需重新标定行距。缺字体时报错，不悄悄换字体或随文件分发商业字体。

## 组件与编译

匿名 `assets/template/main.tex` 是可运行的完整例子，涵盖封面、声明、题名、中英摘要、目录、四级标题、长表、来源、公式、每页脚注、文献和附录。接口和长表规则见 `references/usage.md`。

`python3 scripts/build.py /项目/main.tex --out /项目/build`：XeLaTeX禁用shell escape，多轮至目录与引用稳定，记录哈希和警告。默认脚本位置不是论文源位置，必须传入源文件。失败留下的PDF不是交付物。

`python3 scripts/inspect_pdf.py /项目/build/main.pdf --out /项目/review`：需PyMuPDF与Pillow，生成16页总览、全页尺寸/页码/边界/小字检查及JSON。输出目录必须不存在。先看全部总览，再放大封面、目录、宽表/续表、长公式、文献及标记页。

## Word 交付与版面（必读）

走 Word 路线（python-docx、docx-js 等自写脚本）时，本 Skill 的页面与字号参数只是一部分；表格设计、插图位置、留白、目录、公式与数字的规则见 `references/word-layout-rules.md`，**排版前必须先读**。要点：表格内容由作者定，排版只渲染；先文后图、一页不超过两张图、两图之间必须有正文；目录统一一个右对齐制表位；公式用行内 OMML、一行一条；交付前看全部页缩略总览并按清单逐项检查。

## 格式检查中最容易漏的事

- 列宽要扣单元格内边距；宽表先缩padding或换列布局，不用整体缩放把字压小。负号、数字、括号和显著星号不得因窄列拆坏。
- 表题上、图题下；长表重复标题和列头，注释及来源只在末页；不要让数值行落进表头或表尾。
- 公式用自动全局编号与数学环境换行；保持数学token与原稿一致。圈号优先使用现有中文字体①～⑩，避免TNR缺字。
- 自定义大标题先建PDF锚点再写目录；不能手填页码。中摘、英摘、目录各起1，正文再起1后连续。
- `whcreferences`只提供版式，不核实题录事实；已核定文献内容逐条保持。脚注、表注、参考文献有各自字号与缩进。

交付编译记录、检查结果、字体映射和未解决问题。编译成功与自动筛查都不能证明零差错；明确哪些页做了放大视觉核验。Skill本体不代表上传原稿、联网转换、安装后台任务或覆盖现有论文的授权。
