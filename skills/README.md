# Skills：哪一步用哪个，不同路线不一样

这些 Skill 是给 AI 用的“专项做法说明”，每个文件夹里的 `SKILL.md` 就是正文。路线定义见 Emergence 的 `workflow/01-topic-and-route.md`：

- A1 二手数据实证
- A2 问卷实证
- B1 调查诊断与对策
- B2 案例分析与对策

## 一　怎么用

| 你用的 AI | 用法 |
|---|---|
| Claude Code | 把需要的文件夹复制到 `~/.claude/skills/`；`nature-*` 系列要连同 `nature-shared` 一起复制 |
| Codex 等能装 Skill 的工具 | 按该工具的说明，放进它的 skills 目录 |
| 只能聊天的 AI（ChatGPT 网页版、豆包等） | 到了对应步骤，打开下表里的 `SKILL.md`，让 AI 先读一遍再做；读不了链接的，把文件内容粘贴过去 |

**适配原则**：这些 Skill 多数是为投稿期刊写的。本科论文只借用其中的**检查方法**，不要因为 Skill 建议就加更复杂的模型或分析。判断标准仍是 Emergence 的“及格线”和“必须改”。

## 二　对照表

### 各路线都用

| 步骤 | Skill | 用来做什么 |
|---|---|---|
| 1 定题目与路线 | `nature-social-science` | 把兴趣变成能回答的研究问题，检查题目是否可行、主张是否说过头 |
| 2 找文献 | `literature-downloader` | 生成检索词，合法获取全文，整理题录 |
| 2 找文献 | `nature-reader` | 读原文，核对某个观点到底有没有被这篇文献支持 |
| 2、16 核对文献 | `nature-ref-verifier` | 逐条核对作者、年份、题名、期刊、页码、DOI |
| 3 设计 | `nature-social-science` | 理清概念、机制和证据路线，写清主张的上限 |
| 10 写初稿 | `nature-writing` | 组织章节和论证；只借结构和自查清单，章节结构按学校要求 |
| 12 排版（LaTeX） | `wuhan-college-thesis-latex` | 学校文经管类 LaTeX 模板：封面、目录、三线表、公式、页码 |
| 12 排版（Word） | `../word-tools/layout-rules.md` | Word 版面规则：先文后图、表格、目录、留白 |
| 13 AI 审稿 | `nature-reviewer` | 模拟审稿，找出稿件内部的矛盾；只采纳“必须改” |
| 13 改文字 | `academic-humanizer` | 去掉 AI 腔，校准论断强度，不改数字和引用 |
| 13 改文字 | `humanizer` | 检查套话、机械对比、重复收尾 |
| 13 改文字 | `anti-defensive-writing` | 删掉多余的免责声明和空泛让步，必要的局限保留 |
| 13 润色 | `nature-polishing` | 精简、润色已有文字，或翻译英文摘要 |
| 17 答辩 | `nature-paper2ppt` | 从论文生成答辩 PPT 和讲稿 |

### 按路线加用

| 路线 | 步骤 | Skill | 用来做什么 |
|---|---|---|---|
| A1 二手数据实证 | 7–9 分析与核对 | `nature-statistics` | 核对样本量、系数、区间，确保正文与表格的数值一致 |
| A2 问卷实证 | 8–9 分析与核对 | `nature-statistics` | 同上；另外检查信效度指标的报告是否完整 |
| B1 调查诊断与对策 | 8 诊断分析 | `nature-statistics` | 核对描述统计、差异分析的数字和表述 |
| B1 调查诊断与对策 | 9 短板与对策 | `nature-social-science` | 检查短板的证据够不够，以及对策是否说过头 |
| B2 案例分析与对策 | 5–8 资料与诊断 | `nature-reader` | 读年报、招股说明书、行业报告，摘证据并记出处 |
| B2 案例分析与对策 | 8–9 诊断与对策 | `nature-social-science` | 检查诊断结论和证据是否对得上 |

### 进阶（本科论文一般用不到，老师要求时再看）

这些在原作者仓库，未放进本仓库：

| 路线 | Skill | 地址 |
|---|---|---|
| A1 | `smj-data-analysis`：面板数据、内生性 | https://github.com/brycewang-stanford/Awesome-Journal-Skills |
| A2 | `amj-data-analysis`：测量效度、共同方法偏差、SEM | 同上 |
| B2 | `asq-data-analysis`：质性资料编码、从资料到理论 | 同上 |
| 全部 | `nsfc-figure`：框架图、技术路线图 | https://github.com/njzjz/nsfc-agent-skills |

## 三　来源与许可

| Skill | 来源 | 许可 |
|---|---|---|
| `nature-social-science`、`nature-reader`、`nature-ref-verifier`、`nature-reviewer`、`nature-polishing`、`nature-statistics`、`nature-writing`、`nature-paper2ppt`、`nature-shared` | https://github.com/Yuan1z0825/nature-skills | Apache-2.0（`LICENSES/nature-skills-Apache-2.0.txt`） |
| `humanizer` | https://github.com/blader/humanizer | MIT（文件夹内 LICENSE） |
| `academic-humanizer` | https://github.com/AIScientists-Dev/academic-humanizer | MIT（文件夹内 LICENSE） |
| `anti-defensive-writing` | https://github.com/Kiterlin/anti-defensive-writing | MIT（`LICENSES/anti-defensive-writing-MIT.txt`） |
| `literature-downloader` | 作者 zzcx | MIT（文件夹内 LICENSE） |
| `wuhan-college-thesis-latex` | 本组整理 | — |

第三方 Skill 按原样收录，未作修改。原作者更新后，以原仓库为准。
