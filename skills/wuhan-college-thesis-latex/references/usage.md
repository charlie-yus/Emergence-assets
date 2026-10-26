# 参数与接口

## 学校规范与实现取值

A4；上30/下25/左25/右20 mm；正文12bp宋体类/TNR、首缩2汉字、1.25倍；一级16bp宋体粗居中、二级14bp粗、三级12bp粗、四级12bp正常，编号一、（一）1．（1）。引论、结语及栏目总标题18bp；声明22bp；封面主标题36bp黑体粗，信息14bp仿宋粗。表图题12bp宋体粗，图表全局编号；脚注/资料来源9bp；文献10.5bp单倍，首行2字、续行4.2字；致谢固定23bp。

当前本机无网格基线：正文19.95bp、声明14bp/1.5倍27.75bp、文献14.2bp；是当前字体与LibreOffice试样的近似标定，不是所有Word引擎的普适公式。目录默认采用明文1.25倍；原DOC部分条目1.5倍，保留这一差异。标题前后防碰撞间距是模板实现取值，不能宣称学校明文要求所有这些间距。页眉线距纸上59.903bp，与原DOC直转PDF吻合；不为替代字体的字基线偏差移动横线。

原件DOC网格经LibreOffice会膨胀到39/46.8bp正文/声明行距并撕裂封面；禁止复制这些意外分页。完整差异见format-decisions.md。Windows字体下若未经重新标定，不应宣称与macOS样本等价。

## 最小调用

```tex
\documentclass{whcthesis} % 有学校指定字体后可选[ strictfonts ]
\WhcSetup{title={论文题目},subtitle={},english-title={Thesis Title},author={},english-author={},student-id={},class={},cohort={},major={},school={},supervisor={},supervisor-title={},date={}}
\begin{document}
\WhcMakeCover
\WhcMakeDeclaration
\WhcMakeTitlePage
\begin{whcabstract}[cn]{关键词一；关键词二}摘要原文。\end{whcabstract}
\begin{whcabstract}[en]{Keyword one; Keyword two}Original abstract.\end{whcabstract}
\WhcTableOfContents
\WhcMainMatter
\WhcMajor{引\hspace{2\ccwd}论}[引论]
正文。
\section{研究设计}
\subsection{数据来源}
\subsubsection{测量方法}
\paragraph{具体定义}
正文。
\WhcMajor{结\hspace{2\ccwd}语}[结语]
结语原文。
\begin{whcreferences}
\WhcBibItem{已经核实的原题录，不自动造作者、年份、页码或DOI。}
\end{whcreferences}
\WhcAcknowledgements
% 未提供则留空。
\WhcAppendices
\WhcAppendix{附录题名}
附录原文。
\end{document}
```

可用`cover-title`仅为封面题目设置平衡换行；主`title`和题名页不变。不要改变题目用字。

不要既手写“一、”又调用自动编号section。旧稿若已带编号，应移除仅显示的硬编码编号，或有意采用starred标题并另写目录，不能两套编号叠加。

## 表、图、公式

- 使用booktabs三线表，`\WhcTableFont`（10.5bp为本模板宽表取值）；题目12bp。普通表用tabularx，长表用longtable；具体续表实现见匿名main.tex。
- n列、首尾`@{}`、padding为s时，总内容宽不超过`\linewidth-2(n-1)s`。使用列比例时对每列扣`2(n-1)s/n`。8～9列数字表先尝试2bp padding；不能只看Overfull日志，还要放大检查负数和表头断行。
- `\WhcSource{资料来源或注释}`为9bp楷体、首行2字、后行4字；在表/图容器内调用。长表放入endlastfoot里的跨整行p列，别放endfoot重复每页。
- `equation`自动产生（式1）；`\ref`结果已含“式”，不要再写成“式式1”。长式用aligned/分行但不改变等式。无需给每行手写tag。
- `\WhcBibItem`不提供biblatex引用解析。使用DOI等长串时可用专门可断行宏，但不得对所有反斜杠字符串做全局替换，避免把`\textcircled`这类宏破坏成普通字符串。

## 编译与验收边界

build.py找PATH中的xelatex或本机~/texlive/2026/bin/universal-darwin/xelatex，可用--engine指定。至少3轮、最多6轮，辅助文件不稳定则失败；不得用部分PDF充当完成。每次输出目录可复用，但脚本会先撤销旧成功记录；最终warnings_requiring_review非空需人工裁决。不要交付aux/log当作源文件。

自动页尺寸允许0.6bp舍入差；小于7bp的上标脚注会标记，但脚注正文应9bp。空致谢可被标稀疏页，这是用户要求；其他空白页逐一解释。表内自带源图文字无法靠PDF文本框字号检查代替，应另看原图。

本Skill针对LaTeX和PDF；Word需单独转换与渲染核验，不能把本PDF通过检查当成Word已符合学校规范。
