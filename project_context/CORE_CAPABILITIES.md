# Core Capability Map

本文件记录当前真实代码已经具备的 Core 能力、限制与成熟度。

成熟度定义：
- `Stable`：能力边界已经稳定。
- `Reviewing`：已有可用能力，但已发现限制，正在评估。
- `Upgrade Candidate`：已有明确能力缺口，需要后续升级。

## Template Reader Core

职责（Responsibility）：
- 识别模板文件类型并读取模板基础信息。

当前支持（Current Capabilities）：
- 真实读取 Excel 工作表、非空或有样式单元格、合并区域、行高和列宽。
- 使用真实行列范围判断 Excel 合并单元格。
- 识别 `.xlsx`、`.xlsm`、`.pdf`、`.docx` 和 `.doc`。
- 通过统一读取入口分发到 Excel、PDF 或 Word Reader。

当前限制（Current Limitations）：
- PDF Reader 只校验文件并返回基础文件信息，不解析内容。
- Word Reader 只校验文件并返回基础文件信息，不解析内容。
- 尚未形成跨 Excel、PDF、Word 一致的深度模板读取结果。

成熟度（Maturity）：
- `Reviewing`

升级方向（Upgrade Direction）：
- 评估 PDF、Word 内容读取能力及跨格式读取结果的一致性。

## Field Core

职责（Responsibility）：
- 识别字段标签候选，标准化字段名称，并提供基础字段匹配。

当前支持（Current Capabilities）：
- 基于单元格文本、关键词和冒号规则识别字段标签候选。
- 构造 `FieldCandidate`。
- 对有限的常见中文字段执行标准 key 映射。
- 提供完全相等、包含关系的简单字段匹配。

当前限制（Current Limitations）：
- 字段识别依赖简单文本启发式规则。
- 标准化词表覆盖有限。
- 未使用上下文、表格结构或语义信息判断字段。
- 不提供 AI 语义匹配。

成熟度（Maturity）：
- `Reviewing`

升级方向（Upgrade Direction）：
- 基于真实模板审计扩展字段识别、标准化和上下文匹配能力。

## Table Core

职责（Responsibility）：
- 识别表格、表头、合并单元格及表格范围候选。

当前支持（Current Capabilities）：
- 构造 `TableRangeCandidate`。
- 识别同一行中至少三个非空文本单元格形成的表头候选。
- 基于文本单元格分布生成基础表格候选。
- 将 Excel 合并区域转换为 `MergedCellCandidate`。

当前限制（Current Limitations）：
- 表格边界和数据结束行仍使用简化规则。
- 不支持复杂多行表头、跨行跨列表格及嵌套表格判断。
- 不识别真实数据行语义。
- 不负责表格数据自动填充。

成熟度（Maturity）：
- `Upgrade Candidate`

升级方向（Upgrade Direction）：
- 基于真实复杂模板审计表格边界、表头层级和数据区域识别能力。

## Visual Core

职责（Responsibility）：
- 提供统一坐标模型，以及视觉区域、布局区域和锚点的结构化表达。

当前支持（Current Capabilities）：
- 统一使用 `Coordinate` 表达 Excel、PDF 和 Word 坐标。
- 使用 `CoordinateGroup` 组织多个坐标。
- 构造 `VisualRegionCandidate`、`LayoutRegionCandidate` 和 `AnchorCandidate`。
- 提供 Excel 单元格坐标和 Word 结构坐标构造辅助函数。

当前限制（Current Limitations）：
- 当前候选函数只结构化输入，不执行复杂视觉识别。
- 尚未验证统一坐标对复杂 PDF、Word 布局的完整表达能力。
- 不提供区域关系和布局语义推断。

成熟度（Maturity）：
- `Reviewing`

升级方向（Upgrade Direction）：
- 使用真实 PDF、Word 模板验证坐标表达范围，并评估视觉区域与锚点识别能力。

## Image Core

职责（Responsibility）：
- 表达图片区域候选和图片锚点候选。

当前支持（Current Capabilities）：
- 构造 `ImageAreaCandidate`。
- 构造 `ImageAnchorCandidate`。
- 使用现有 `Coordinate` 表达图片区域和锚点位置。

当前限制（Current Limitations）：
- 不读取或分析真实图片文件。
- 不从模板中自动检测图片区域或锚点。
- 不验证图片内容、尺寸或格式。
- 不执行图片插入。

成熟度（Maturity）：
- `Upgrade Candidate`

升级方向（Upgrade Direction）：
- 基于真实模板审计图片区域、锚点和图片输入的识别需求。

## Condition Core

职责（Responsibility）：
- 表达基础条件候选、条件规则并计算条件结果。

当前支持（Current Capabilities）：
- 构造 `ConditionCandidate`。
- 使用 `ConditionRule` 表达条件。
- `evaluate_condition` 支持 `equals` 和 `not_equals`。

当前限制（Current Limitations）：
- 不支持 `AND`、`OR`、嵌套条件或复杂表达式。
- 不负责自动发现条件关系。
- 不负责流程编排或页面联动。

成熟度（Maturity）：
- `Reviewing`

升级方向（Upgrade Direction）：
- 根据真实条件模板评估现有操作符和条件组合能力是否足够。

## Choice Core

职责（Responsibility）：
- 表达选择候选、选择项和单选或多选结果。

当前支持（Current Capabilities）：
- `options`
- `allow_multiple`
- `default_option`
- 校验单选数量和非法选项值。
- 生成带选中状态的选择结果。

当前限制（Current Limitations）：
- 不支持 option coordinate。
- 不支持 checkbox choice。
- 不支持 radio choice。
- 不支持位置型选择。

成熟度（Maturity）：
- `Upgrade Candidate`

升级方向（Upgrade Direction）：
- 支持位置型选择能力。
- 当前不决定最终实现方案或最终命名。

### Choice Core Upgrade Design

当前 Choice Core 职责：
- 表达模板中的选择类业务。

当前已支持：
- `options`。
- `allow_multiple`。
- `default_option`。
- 简单值选择。

当前无法支持：
- option coordinate。
- checkbox choice。
- radio choice。
- dropdown choice。
- multiselect position choice。
- 选项到模板坐标的映射。

真实业务类型：
- Value Choice：选择后写入一个普通值。
- Checkbox Choice：选项对应可勾选位置。
- Radio Choice：多个选项互斥，选项对应位置。
- Dropdown Choice：模板中存在下拉或等价选择结构。
- MultiSelect Choice：允许多个选项同时选中。

设计原则：
- Choice Core 的判断标准是能力，不是名字。
- 不因名字不专业而重命名。
- 只有当真实能力边界要求时，才升级结构。
- Choice Core 可以作为选择类业务核心继续存在。
- 是否升级为更大概念，后续根据真实业务和代码成本决定。

建议数据能力：
- `choice_mode`。
- `options` 使用结构化 option objects。
- option object 可表达 `option_key`、`label`、`value`、`coordinate`、`selected` 和 `metadata`。
- `selected_values`。
- `option_targets`。

后续升级路线：
1. 扩展 `ChoiceCandidate` / `ChoiceOption`。
2. 扩展 `TemplateAnalysisResult`。
3. 扩展 `ChoiceNode`。
4. 同步 `WorkspaceChoice`。
5. 同步 `ConfirmedChoice`。
6. 扩展 ExportStrategy，支持 `set_choice`。
7. Executor 的真实 checkbox / radio 写入单独处理。

## Matching Core

职责（Responsibility）：
- 将 `OrderObject` 中的字段与 `DocumentModel` 字段进行候选匹配。

当前支持（Current Capabilities）：
- 构造 `CandidateFillObject` 和 `CandidateFillField`。
- 根据字段 key 完全相等或包含关系计算分数。
- 按最低分数阈值选择字段候选。
- 记录未匹配字段、警告和基础来源信息。

当前限制（Current Limitations）：
- 只匹配字段 key，不使用标签、上下文或语义信息。
- 不支持多候选排序、冲突处理或人工映射配置。
- 不处理表格、图片或选择对象。
- 不提供 AI 语义匹配。

成熟度（Maturity）：
- `Upgrade Candidate`

升级方向（Upgrade Direction）：
- 基于真实订单和模板审计字段候选排序、上下文匹配及非字段对象匹配需求。

## AI Parser Core

职责（Responsibility）：
- 表达结构化订单对象，并提供订单文本解析入口和提示词构造能力。

当前支持（Current Capabilities）：
- 定义 `OrderObject`、`OrderField`、`MissingField` 和 `ParseResult`。
- 使用 stub 解析器处理按行排列的 `key:value` 文本。
- 构造包含预期字段的订单解析提示词。

当前限制（Current Limitations）：
- 当前解析器是 stub，不调用真实 AI 模型。
- 不处理复杂自然语言、表格、附件或图片订单。
- 不包含模型调用、结构化响应校验或重试机制。
- 提示词构造与真实 AI Runtime 尚未接通。

成熟度（Maturity）：
- `Upgrade Candidate`

升级方向（Upgrade Direction）：
- 在 AI Runtime 阶段基于真实订单样本评估解析、响应校验和错误处理需求。

## Executor Core

职责（Responsibility）：
- 按 `ExportStrategy` 中的 `ExportOperation` 执行文件导出，并记录操作结果。

当前支持（Current Capabilities）：
- Excel Executor 支持 `write_value`。
- Excel Executor 提供 `write_table` 写入能力。
- Excel Executor 对 `insert_image` 执行目标校验并记录 skipped。
- Word Executor 支持 `.docx` 中 `word/document.xml` 的 placeholder 替换。
- PDF Executor 复制原 PDF，并为操作记录 skipped。
- 提供执行成功、跳过和失败统计。

当前限制（Current Limitations）：
- 当前 `write_table` Executor 需要二维 list，但现有表格导出计划使用描述性 dict，接口尚未对齐。
- Excel 不执行真实图片插入。
- Word 不支持复杂表格、bookmark 真实定位或图片插入。
- PDF 不执行真实写入。
- Excel 使用独立结果对象，尚未完全统一到通用执行结果模型。

成熟度（Maturity）：
- `Upgrade Candidate`

升级方向（Upgrade Direction）：
- 优先审计并对齐 ExportOperation 与各 Executor 的输入契约，再评估真实图片、PDF 和 Word 写入能力。
