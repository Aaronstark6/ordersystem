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
- 表达条件规则、业务规则和联动规则，并计算基础条件结果。

当前支持（Current Capabilities）：
- 构造 `ConditionCandidate`。
- 使用 `ConditionRule` 表达条件。
- `evaluate_condition` 支持 `equals` 和 `not_equals`。
- ConditionPolicy V1 支持 `equals`、`not_equals`、`is_empty`、`not_empty` 和 `contains`。
- ConditionPolicy V1 支持 `export` 和 `skip_export`。
- ConditionPolicy V1 可在 operation 生成前跳过受控节点。
- ConditionPolicy V1 可从 ConfirmedField / ConfirmedChoice 最终事实解析条件实际值。

当前限制（Current Limitations）：
- Core ConditionEvaluator 仍只支持 `equals` 和 `not_equals`。
- 不支持 `AND`、`OR`、嵌套条件或复杂表达式。
- 不负责自动发现条件关系。
- 不负责流程编排或页面联动。
- `show`、`hide`、`enable` 和 `disable` 尚未实现。

成熟度（Maturity）：
- `Upgrade Candidate`

升级方向（Upgrade Direction）：
- 统一 Core ConditionEvaluator 与 ConditionPolicy 的操作符能力，并补齐非导出联动行为。

Condition V1 定位：
- Condition 表达条件规则、业务规则和联动规则。
- Condition 不直接生成 ExportOperation。
- Condition 通过 ExportPolicy 影响 ExportStrategy 中导出动作的生成。
- ConditionPolicy V1 已实现 `export` 与 `skip_export`。
- Condition V1 范围只包含 `equals`、`not_equals`、`is_empty`、`not_empty` 和 `contains`。
- Condition V1 不包含 `AND`、`OR`、嵌套条件或复杂表达式。

Condition V1 控制对象：
- Field。
- Choice。
- Table。
- Image。
- Section。

Condition V1 控制行为：
- `show`。
- `hide`。
- `enable`。
- `disable`。
- `export`。
- `skip_export`。

## Choice Core

职责（Responsibility）：
- 表达选择候选、选择项和单选或多选结果。

当前支持（Current Capabilities）：
- `options`
- `allow_multiple`
- `default_option`
- `ChoiceCandidate.choice_mode`
- `ChoiceOption.coordinate`
- Choice Contract 已升级。
- DocumentModel ChoiceNode 已承载 `choice_mode` 与 `option_details`。
- WorkspaceChoice 已承载 `choice_mode`、`option_details` 与 `selected_values`。
- ConfirmedChoice 已承载 `choice_mode`、`option_details`、`selected_values` 与 `final_selected_values`。
- Choice 已传播到 ExportStrategy。
- `set_choice` 已成为选择类导出计划操作。
- `set_choice` 已进入 Excel Executor 第一版。
- 校验单选数量和非法选项值。
- 生成带选中状态的选择结果。

当前限制（Current Limitations）：
- 已开始契约升级，但尚不自动识别 checkbox、radio 或 dropdown。
- Excel Executor 已支持 checkbox、radio 和 multiselect 的坐标型勾选写入。
- Word / PDF Executor 尚未支持 `set_choice`。

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
- `ChoiceCandidate` 已具备 `choice_mode` 承载能力。
- `ChoiceOption` 已具备 option coordinate 承载能力。
- `ChoiceNode` 已具备 `choice_mode` 与 `option_details` 承载能力。
- `WorkspaceChoice` 已具备 `choice_mode`、`option_details` 与 `selected_values` 承载能力。
- `ConfirmedChoice` 已具备 `final_selected_values` 承载能力。
- ConfirmedChoice 已可生成 `ExportOperation(set_choice)`。
- Excel Executor 已可执行第一版 `set_choice`。

当前无法支持：
- checkbox、radio、dropdown 的自动识别。
- multiselect position choice 的自动识别。
- Word / PDF Executor 对位置型选择的真实写入。
- 选项到导出目标的完整映射与执行。

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
6. 已扩展 ExportStrategy，支持 `set_choice`。
7. Excel Executor 已支持第一版 checkbox / radio / multiselect 坐标写入。
8. Word / PDF Executor 的真实选择写入仍需单独处理。

### Choice Middle Layer Model Design

ChoiceNode 职责：
- 保存模板事实。
- 保存 `choice_mode`。
- 保存 `option_details`。
- 保存选项坐标。
- 不保存用户最终确认结果。

WorkspaceChoice 职责：
- 保存用户确认前的中层表达。
- 面向用户确认。
- 可以保存 AI 或系统建议选择。
- 可以使用 `selected_values` 表达建议选择或当前工作区选择。
- 不保存最终确认事实。
- 不生成导出操作。

ConfirmedChoice 职责：
- 保存人工确认后的最终选择事实。
- 对 value choice 可以继续保留 `final_value`。
- 对 checkbox_group、radio_group 和 multiselect 应支持 `final_selected_values`。
- 是 ExportStrategy 的选择事实来源。

WorkspaceChoice 字段设计建议：
- `choice_key`。
- `label`。
- `node_id`。
- `choice_mode`。
- `options`。
- `option_details`。
- `allow_multiple`。
- `default_option`。
- `value`。
- `selected_values`。
- `coordinate`。
- `metadata`。
- `editable`。
- `required`。
- `warnings`。
- `errors`。

ConfirmedChoice 字段设计建议：
- `choice_key`。
- `label`。
- `node_id`。
- `choice_mode`。
- `options`。
- `option_details`。
- `original_value`。
- `user_value`。
- `final_value`。
- `selected_values`。
- `final_selected_values`。
- `confirmed`。
- `coordinate`。
- `metadata`。

`value` 与 `selected_values` 的关系：
- `value` / `final_value` 适合 value choice。
- `selected_values` / `final_selected_values` 适合 checkbox_group、radio_group 和 multiselect。
- 过渡期可以同时保留两类字段，避免破坏旧链路。
- 后续生成导出计划时，由 `choice_mode` 决定使用 `final_value` 还是 `final_selected_values`。

中层升级顺序：
1. 升级 WorkspaceChoice 数据表达。
2. 同步 ChoiceNode → WorkspaceChoice Builder。
3. 升级 ConfirmedChoice 数据表达。
4. 同步 WorkspaceChoice → ConfirmedChoice Builder。
5. 验证 value choice 旧链路兼容。
6. 后续单独升级 ExportStrategy 的选择计划。
7. Executor 的真实位置型选择写入不在中层模型升级中处理。

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
- Excel Executor 支持第一版 `set_choice`。
- Word Executor 支持 `.docx` 中 `word/document.xml` 的 placeholder 替换。
- PDF Executor 复制原 PDF，并为操作记录 skipped。
- 提供执行成功、跳过和失败统计。

当前限制（Current Limitations）：
- 当前 `write_table` Executor 需要二维 list，但现有表格导出计划使用描述性 dict，接口尚未对齐。
- Excel 不执行真实图片插入。
- Word / PDF 不执行 `set_choice`。
- Word 不支持复杂表格、bookmark 真实定位或图片插入。
- PDF 不执行真实写入。
- Excel 使用独立结果对象，尚未完全统一到通用执行结果模型。

成熟度（Maturity）：
- `Upgrade Candidate`

升级方向（Upgrade Direction）：
- 优先审计并对齐 ExportOperation 与各 Executor 的输入契约，再评估真实图片、PDF 和 Word 写入能力。
# Field Detection Reality Upgrade V1

状态：
- Field Detector 已完成 Reality Upgrade V1。
- Field Detector 仍是 `Upgrade Candidate`，不标记为 `Stable`。

已补齐：
- 支持常见中文字段标签。
- 支持常见英文字段标签，英文匹配大小写不敏感。
- 支持英文冒号 `:` 与中文冒号 `：`。
- 支持去除冒号和空白后再判断 label hint。
- 支持最小 `target_cell` 推断，并以候选对象运行时 metadata 形式预留。

当前边界：
- 不修改 `FieldLabelCandidate` 合同。
- 不修改 DocumentModel / Workspace / Confirmed / Export / Executor。
- 不支持复杂合并单元格推断。
- 不支持跨区域搜索。
- 不负责 Choice / Condition / Table / Image 识别。

# Template Analysis Reality Gap

来源：`STAGE3_REALITY_VALIDATION_RUN_01`。

真实验证结果：
- Field = 0。
- Choice = 0。
- Condition = 0。
- Image = 0。
- Table = 13。
- ExportStrategy 只生成 `write_table`。
- Excel Executor 的 `table start_cell` 报错是后续执行契约问题，不是当前 Template Analysis 主要断点。

当前判断：
- 下游主链结构已经较完整：DocumentModel、Workspace、Confirmed、ExportStrategy、Excel Executor 均可被真实链路调用。
- 当前最大断点位于上游 Template Analysis 与 Detector 层。
- Pipeline 已完成不等于 Detection 已完成。

当前能力缺口：
- Field Detection 弱，真实模板中未产出字段；需补齐中英文标签、冒号字段、相邻空白目标格等规则。
- Choice Detection 未真正实现；Choice Pipeline 已完成，但真实模板未产出 ChoiceCandidate。
- Condition Detection 未真正实现；Condition Pipeline / ConditionPolicy 已完成，但真实模板未产出 ConditionCandidate。
- Image Detection 未真正实现；Image Pipeline 已完成，但真实模板未产出 ImageAreaCandidate / ImageAnchorCandidate。
- Table Detection 过于激进，误把普通布局识别为 Table。

状态标记：
- Template Analysis：`Upgrade Candidate`
- Field Detector：`Upgrade Candidate`
- Choice Detector：`Upgrade Candidate`
- Condition Detector：`Upgrade Candidate`
- Image Detector：`Upgrade Candidate`
- Table Detector：`Reviewing`

升级原则：
- Template Analysis 后续升级以 detector 能力补齐为主。
- 不直接重写 Template Analysis。
- 不把 Field / Choice / Condition / Image / Table 识别规则塞进 `app/core/template_analysis/analyzer.py`。
- detector 文件保持小职责；超过约 200 到 300 行再评估拆分。
# Choice Detection V1

状态：
- Choice Detector 已进入 V1。
- Choice Detector 仍是 `Upgrade Candidate`，不标记为 `Stable`。

已支持：
- Checkbox marker 识别。
- Radio marker 识别。
- Yes / No 识别。
- 常见二选一识别：Male / Female、Domestic / Export、Sample / Production。
- 产出既有 `ChoiceCandidate`，并保留 option coordinate 与 `choice_mode`。

当前边界：
- 不新增第二套 Choice Contract。
- 不修改 DocumentModel / Workspace / Confirmed / ExportStrategy / Executor。
- 不支持 Dropdown。
- 不支持复杂 MultiSelect 或跨区域复杂分组。
# Image Detection V1 Update

- Image Detection V1 已开始支持图片占位文字识别。
- 支持英文关键词：image、product image、label image、package image、packaging image、logo、stamp、signature。
- 支持中文关键词：图片、产品图片、标签图片、包装图片、商标、印章、签名。
- 可推断 image_role：logo、product_image、label_image、package_image、stamp、signature、generic_image。
- 当前仍为 Upgrade Candidate。
- 当前不扫描真实嵌入图片、不推断图片尺寸、不绑定图片文件、不处理复杂锚点。
# Table Detector Guardrail V1

- Table Detector Guardrail V1 目标是减少误判，不是增强复杂表格能力。
- 已避免把明显字段布局行、choice 行、image placeholder 行和 validation/control mapping 行识别为 table。
- Table V1 候选需要表头证据，并且需要数据行或明确 table 标题。
- 当前仍不做复杂表格引擎、不修改 table export contract、不修改 Excel Executor。
