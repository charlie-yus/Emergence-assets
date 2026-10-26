\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{whcthesis}[2026/10/24 Wuhan College humanities/economics/management thesis]
\newif\ifwhcstrictfonts
\DeclareOption{strictfonts}{\whcstrictfontstrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{ctexart}}
\ProcessOptions\relax
\LoadClass[UTF8,fontset=none,zihao=-4,a4paper]{ctexart}
\RequirePackage{iftex}
\RequireXeTeX
\RequirePackage[top=30mm,bottom=25mm,left=25mm,right=20mm,headheight=12bp,headsep=9mm,footskip=7.5mm]{geometry}
\RequirePackage{fontspec,graphicx,booktabs,longtable,tabularx,array,amsmath,amssymb,fancyhdr,caption,needspace,xkeyval}
\RequirePackage[perpage,bottom]{footmisc}
\RequirePackage[hidelinks,unicode,hypertexnames=false]{hyperref}
\InputIfFileExists{local-fonts.tex}{}{\ClassError{whcthesis}{local-fonts.tex is required}{Use the supplied font profile or configure the four required Chinese families.}}
\linespread{1}
\makeatletter
\renewcommand\normalsize{\@setfontsize\normalsize{12bp}{\whcbodybaseline}\abovedisplayskip=10bp\belowdisplayskip=10bp\abovedisplayshortskip=5bp\belowdisplayshortskip=5bp}
\renewcommand\small{\@setfontsize\small{10.5bp}{\whcreferencebaseline}}
\renewcommand\footnotesize{\@setfontsize\footnotesize{9bp}{12bp}}
\makeatother
\normalsize
\xeCJKDeclareCharClass{CJK}{"2460 -> "2469}
\setlength\parindent{2\ccwd}
\setlength\parskip{0bp}
\setlength\emergencystretch{1\ccwd}
\setlength\tabcolsep{5bp}
\setlength\LTpre{6bp}
\setlength\LTpost{6bp}
\renewcommand\arraystretch{1.15}
\newcommand\WhcBodyFont{\songti\normalfont\fontsize{12bp}{\whcbodybaseline}\selectfont}
\newcommand\WhcSource[1]{\par\begingroup\kaishu\fontsize{9bp}{12bp}\selectfont\leftskip=4\ccwd\rightskip=0pt\parfillskip=0pt plus1fil\parindent=-2\ccwd\indent #1\par\endgroup}
\newcommand\WhcTableFont{\songti\fontsize{10.5bp}{\whcreferencebaseline}\selectfont}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\newcolumntype{C}[1]{>{\centering\arraybackslash}p{#1}}
\newcolumntype{R}[1]{>{\raggedleft\arraybackslash}p{#1}}
\newcolumntype{Y}{>{\raggedright\arraybackslash}X}
\fancypagestyle{whc}{\fancyhf{}\fancyhead[C]{\songti\fontsize{9bp}{12bp}\selectfont 武汉学院毕业论文（设计）}\fancyfoot[C]{\rmfamily\fontsize{9bp}{12bp}\selectfont\thepage}\renewcommand\headrulewidth{0.75bp}\renewcommand\footrulewidth{0bp}}
\fancypagestyle{whc-nonum}{\fancyhf{}\fancyhead[C]{\songti\fontsize{9bp}{12bp}\selectfont 武汉学院毕业论文（设计）}\renewcommand\headrulewidth{0.75bp}\renewcommand\footrulewidth{0bp}}
\fancypagestyle{plain}{\fancyhf{}\fancyhead[C]{\songti\fontsize{9bp}{12bp}\selectfont 武汉学院毕业论文（设计）}\fancyfoot[C]{\rmfamily\fontsize{9bp}{12bp}\selectfont\thepage}\renewcommand\headrulewidth{0.75bp}\renewcommand\footrulewidth{0bp}}
\ctexset{
 section={format={\centering\songti\bfseries\fontsize{16bp}{24bp}\selectfont},name={},number=\chinese{section},tocline={\CTEXifname{\protect\numberline{\CTEXthesection、}}{}#2},aftername={、},beforeskip=15.6bp,afterskip=15.6bp,fixskip=true,afterindent=true},
 subsection={format={\songti\bfseries\fontsize{14bp}{23.275bp}\selectfont},name={},number={（\chinese{subsection}）},aftername={},indent=2\ccwd,beforeskip=12bp,afterskip=8bp,fixskip=true,afterindent=true},
 subsubsection={format={\songti\bfseries\fontsize{12bp}{\whcbodybaseline}\selectfont},name={},number=\arabic{subsubsection},aftername={．},indent=2\ccwd,beforeskip=8bp,afterskip=5bp,fixskip=true,afterindent=true},
 paragraph={format={\songti\normalfont\fontsize{12bp}{\whcbodybaseline}\selectfont},name={},number={（\arabic{paragraph}）},aftername={},indent=2\ccwd,beforeskip=5bp,afterskip=5bp,runin=false,afterindent=true}}
\setcounter{secnumdepth}{4}
\setcounter{tocdepth}{2}
\AddToHook{cmd/section/before}{\Needspace{4\baselineskip}}
\AddToHook{cmd/subsection/before}{\Needspace{3\baselineskip}}
\AddToHook{cmd/subsubsection/before}{\Needspace{3\baselineskip}}
\AddToHook{cmd/paragraph/before}{\Needspace{3\baselineskip}}
\DeclareCaptionFont{whc}{\songti\bfseries\fontsize{12bp}{\whcbodybaseline}\selectfont}
\DeclareCaptionLabelFormat{whc}{#1#2}
\DeclareCaptionLabelSeparator{whc}{\hspace{2\ccwd}}
\captionsetup{font=whc,labelformat=whc,labelsep=whc,justification=centering,singlelinecheck=false,skip=6bp}
\captionsetup[table]{position=top}
\captionsetup[figure]{position=bottom}
\renewcommand\tablename{表}
\renewcommand\figurename{图}
\renewcommand\theequation{式\arabic{equation}}
\makeatletter
\def\tagform@#1{\maketag@@@{（\ignorespaces#1\unskip\@@italiccorr）}}
\renewcommand\thefootnote{\ifcase\value{footnote}\or ①\or ②\or ③\or ④\or ⑤\or ⑥\or ⑦\or ⑧\or ⑨\or ⑩\else\textcircled{\scriptsize\arabic{footnote}}\fi}
\renewcommand\footnoterule{\kern-3bp\hrule width .3\textwidth height .4bp\kern2.6bp}
\renewcommand\@makefntext[1]{\parindent=2\ccwd\noindent\hb@xt@2\ccwd{\hss\@makefnmark\ }#1}
\newcommand\whctitle{论文题目}
\newcommand\whcsubtitle{}
\newcommand\whccovertitle{\whctitle}
\newcommand\whcenglishtitle{Thesis Title}
\newcommand\whcauthor{}
\newcommand\whcenglishauthor{}
\newcommand\whcstudentid{}
\newcommand\whcclass{}
\newcommand\whccohort{}
\newcommand\whcmajor{}
\newcommand\whcschool{}
\newcommand\whcsupervisor{}
\newcommand\whcsupervisortitle{}
\newcommand\whcdate{}
\newcommand\whclogo{assets/whc-logo.png}
\define@key{whc}{title}{\renewcommand\whctitle{#1}}
\define@key{whc}{cover-title}{\renewcommand\whccovertitle{#1}}
\define@key{whc}{subtitle}{\renewcommand\whcsubtitle{#1}}
\define@key{whc}{english-title}{\renewcommand\whcenglishtitle{#1}}
\define@key{whc}{author}{\renewcommand\whcauthor{#1}}
\define@key{whc}{english-author}{\renewcommand\whcenglishauthor{#1}}
\define@key{whc}{student-id}{\renewcommand\whcstudentid{#1}}
\define@key{whc}{class}{\renewcommand\whcclass{#1}}
\define@key{whc}{cohort}{\renewcommand\whccohort{#1}}
\define@key{whc}{major}{\renewcommand\whcmajor{#1}}
\define@key{whc}{school}{\renewcommand\whcschool{#1}}
\define@key{whc}{supervisor}{\renewcommand\whcsupervisor{#1}}
\define@key{whc}{supervisor-title}{\renewcommand\whcsupervisortitle{#1}}
\define@key{whc}{date}{\renewcommand\whcdate{#1}}
\define@key{whc}{logo}{\renewcommand\whclogo{#1}}
\NewDocumentCommand\WhcSetup{m}{\setkeys{whc}{#1}}
\newcommand\WhcHeading[1]{\par\addvspace{15.6bp}{\centering\songti\bfseries\fontsize{18bp}{27bp}\selectfont #1\par}\nobreak\vspace{15.6bp}\@afterindenttrue\@afterheading}
\NewDocumentCommand\WhcMajor{m O{}}{\clearpage\phantomsection\WhcHeading{#1}\if\relax\detokenize{#2}\relax\addcontentsline{toc}{section}{#1}\else\addcontentsline{toc}{section}{#2}\fi}
\newcommand\WhcResetPages{\clearpage\pagenumbering{arabic}\pagestyle{whc}}
\newcommand\WhcCoverRow[2]{\makebox[22.6mm][s]{#1}&：&\parbox[b]{82.8mm}{\centering\fangsong\bfseries\fontsize{14bp}{\whccoverbaseline}\selectfont #2\strut}\\[-1.2bp]\cline{3-3}\noalign{\vskip3.3mm}}
\newcommand\WhcMakeCover{%
 \clearpage\thispagestyle{empty}\begingroup
 \centering\vspace*{8mm}\IfFileExists{\whclogo}{\includegraphics[width=76mm]{\whclogo}\par}{}
 \vspace{22mm}{\heiti\bfseries\fontsize{36bp}{50bp}\selectfont 本科毕业论文（设计）\par}
 \vspace{22mm}\fangsong\bfseries\fontsize{14bp}{\whccoverbaseline}\selectfont
 \setlength\tabcolsep{1.905mm}\setlength\arrayrulewidth{0.5bp}
 \begin{tabular}{p{22.6mm}p{5.72mm}p{82.8mm}}
 \WhcCoverRow{论文题目}{\whccovertitle\ifx\whcsubtitle\empty\else\par ——\whcsubtitle\fi}
 \WhcCoverRow{姓名}{\whcauthor}
 \WhcCoverRow{学号}{\whcstudentid}
 \WhcCoverRow{班级}{\whcclass}
 \WhcCoverRow{届次}{\whccohort}
 \WhcCoverRow{专业}{\whcmajor}
 \WhcCoverRow{学院（部）}{\whcschool}
 \WhcCoverRow{指导教师}{\whcsupervisor\ifx\whcsupervisortitle\empty\else（\whcsupervisortitle）\fi}
 \WhcCoverRow{完成时间}{\whcdate}
 \end{tabular}\par\endgroup\clearpage}
\newcommand\WhcMakeDeclaration{%
 \clearpage\thispagestyle{whc-nonum}\begingroup
 \vspace*{15.6bp}{\centering\songti\bfseries\fontsize{22bp}{33bp}\selectfont 作者声明\par}\vspace{15.6bp}
 \songti\fontsize{14bp}{\whcdeclarationbaseline}\selectfont\setlength\parindent{2\ccwd}
 本毕业论文（设计）是在导师的指导下由本人独立撰写完成的，没有剽窃、抄袭、造假等违反道德、学术规范和其他侵权行为。对本论文（设计）的研究做出重要贡献的个人和集体，均已在文中以明确方式标明。因本毕业论文（设计）引起的法律结果完全由本人承担。\par
 毕业论文（设计）成果归武汉学院所有。\par
 特此声明\par
 \vspace{22mm}\noindent\hfill\begin{minipage}{96.26mm}\fangsong\fontsize{14bp}{\whccoverbaseline}\selectfont
 \begin{tabularx}{\linewidth}{@{}p{27.78mm}p{9.53mm}Y@{}}
 作者专业&：&\bfseries\whcmajor\\[5mm]
 作者学号&：&\bfseries\whcstudentid\\[5mm]
 作者签名&：&\rule{0pt}{6mm}\\[7mm]
 &\multicolumn{2}{r}{\hspace{7mm}年\hspace{5mm}月\hspace{5mm}日}
 \end{tabularx}\end{minipage}\par\endgroup\clearpage}
\newcommand\WhcMakeTitlePage{%
 \clearpage\thispagestyle{whc-nonum}\begingroup\centering
 \vspace*{124.8bp}
 {\heiti\bfseries\fontsize{22bp}{30bp}\selectfont\whctitle\par\ifx\whcsubtitle\empty\else ——\whcsubtitle\par\fi}
 \vspace{15.6bp}{\heiti\fontsize{16bp}{22bp}\selectfont\whcauthor\par}
 \vspace{15.6bp}{\rmfamily\fontsize{22bp}{30bp}\selectfont\whcenglishtitle\par}
 \vspace{15.6bp}{\rmfamily\fontsize{16bp}{22bp}\selectfont\whcenglishauthor\par}
 \vfill{\songti\bfseries\fontsize{16bp}{22bp}\selectfont\whcdate\par}\vspace*{31.2bp}
 \endgroup\clearpage}
\NewDocumentEnvironment{whcabstract}{O{cn} m}{\WhcResetPages\def\whcabstractlang{#1}\def\whckeywords{#2}\def\whccn{cn}\ifx\whcabstractlang\whccn\WhcHeading{摘\hspace{2\ccwd}要}\else\WhcHeading{Abstract}\fi\WhcBodyFont\ignorespaces}{\par\vspace{\baselineskip}\noindent\ifx\whcabstractlang\whccn{\songti\bfseries\fontsize{16bp}{24bp}\selectfont 关键词：}\else{\rmfamily\bfseries\fontsize{16bp}{24bp}\selectfont Keywords: }\fi{\WhcBodyFont\whckeywords}\par\clearpage}
\renewcommand\l@section[2]{\begingroup\songti\bfseries\fontsize{14bp}{23.275bp}\selectfont\@dottedtocline{1}{0bp}{0bp}{#1}{#2}\endgroup}
\renewcommand\l@subsection[2]{\begingroup\songti\fontsize{12bp}{\whcbodybaseline}\selectfont\@dottedtocline{2}{2\ccwd}{0bp}{#1}{#2}\endgroup}
\newcommand\WhcTableOfContents{\WhcResetPages\WhcHeading{目\hspace{2\ccwd}录}\@starttoc{toc}\clearpage}
\newcommand\WhcMainMatter{\WhcResetPages\WhcBodyFont\setcounter{section}{0}}
\NewDocumentEnvironment{whcreferences}{}{\WhcMajor{参考文献}\begingroup\songti\fontsize{10.5bp}{\whcreferencebaseline}\selectfont\setcounter{whcbib}{0}\leftskip=4.2\ccwd\rightskip=0bp\parindent=-2.2\ccwd}{\par\endgroup}
\newcounter{whcbib}
\NewDocumentCommand\WhcBibItem{m}{\refstepcounter{whcbib}\indent[\arabic{whcbib}]#1\par}
\newcommand\WhcAcknowledgements{\clearpage\par\vspace*{7.8bp}{\centering\songti\bfseries\fontsize{18bp}{27bp}\selectfont 致\hspace{2\ccwd}谢\par}\vspace{7.8bp}\WhcBodyFont\fontsize{12bp}{23bp}\selectfont}
\newcounter{whcappendix}
\newcommand\WhcAppendices{\clearpage\phantomsection\WhcHeading{附\hspace{2\ccwd}录}\addcontentsline{toc}{section}{附录}\setcounter{whcappendix}{0}\WhcBodyFont}
\NewDocumentCommand\WhcAppendix{m}{\ifnum\value{whcappendix}>0\relax\clearpage\fi\refstepcounter{whcappendix}{\noindent\heiti\bfseries\fontsize{16bp}{24bp}\selectfont 附录\chinese{whcappendix}\par}\addcontentsline{toc}{subsection}{附录\chinese{whcappendix}\quad #1}{\centering\songti\bfseries\fontsize{16bp}{24bp}\selectfont #1\par}\WhcBodyFont}
\makeatother
\AtBeginDocument{\WhcBodyFont\pagestyle{whc}}
\endinput
