# 主链

Template
↓
TemplateAnalysisResult
↓
DocumentModel
↓
WorkspaceSnapshot
↓
ConfirmedOrderObject
↓
ExportStrategy
↓
Executor

# 共享主链

- Excel、PDF、Word 共享同一条业务主链。
- 文档类型差异由 Template Reader、Coordinate 和 Executor 能力处理。
- 上游事实对象和流程边界保持一致。

# Pipeline 原则

- Pipeline 只组织流程。
- Pipeline 不实现核心能力。
- Pipeline 不直接写页面。
- Pipeline 不直接做存储细节。
- Pipeline 需要持久化时，通过未来 Storage 层使用 `data/`，不得自行拼接路径写文件。

# 主链存储边界

- Template Reader 读取 `data/templates/`。
- Upload 未来写入 `data/uploads/`。
- Runtime 状态未来写入 `data/runtime/`。
- Cache 未来写入 `data/cache/`。
- Executor 导出未来写入 `data/exports/`。
- Samples 用于真实验证。
- Template Intake Pipeline：读取 `data/templates/` 中的正式模板，或接收并登记 `data/uploads/` 中的用户上传文件。
- Template Analysis Pipeline：读取模板；可通过 Storage 读取或写入 `data/cache/` 中可重新生成的分析缓存，并把当前分析状态写入 `data/runtime/`。
- DocumentModel Pipeline：可通过 Storage 把当前 DocumentModel 运行状态写入 `data/runtime/`。
- Order Parse Pipeline 与 Matching Pipeline：可通过 Storage 使用 `data/cache/` 中可重新生成的 AI 解析和匹配缓存。
- Workspace Pipeline：可通过 Storage 把当前 WorkspaceSnapshot 写入 `data/runtime/`。
- Human Confirm Pipeline：可通过 Storage 把当前 ConfirmedOrderObject 写入 `data/runtime/`。
- Export Strategy Pipeline：只生成导出计划；如需保存当前策略，只能通过 Storage 写入 `data/runtime/`。
- Export Execute Pipeline：读取 `data/templates/` 或已登记上传模板，并把最终结果写入 `data/exports/`。
- `data/samples/` 只作为测试和验证输入，不是生产主链运行状态目录。
- `audit_output/` 不参与任何系统 Pipeline，只用于开发审计临时输出。

# Pipeline 组成

- Template Intake Pipeline。
- Template Analysis Pipeline。
- DocumentModel Pipeline。
- Order Parse Pipeline。
- Matching Pipeline。
- Workspace Pipeline。
- Human Confirm Pipeline。
- Export Strategy Pipeline。
- Export Execute Pipeline。

# Workspace Pipeline

输入：
- DocumentModel。

步骤：
- 保留 SectionNode 的区域组织。
- 将 FieldNode 转换为 WorkspaceField。
- 将 TableNode 转换为 WorkspaceTable。
- 将 ImageNode 转换为 WorkspaceImage。
- 将 ChoiceNode 转换为 WorkspaceChoice。
- 将 ConditionNode 转换为 WorkspaceCondition。

输出：
- WorkspaceSnapshot。
- 承载字段、表格、图片、选择和条件表达。

边界：
- Workspace Pipeline 只组织 DocumentModel 到 WorkspaceSnapshot 的中层表达。
- 不组织页面。
- 不执行导出。

内部组织：
- build_workspace_snapshot 仍是 Workspace Pipeline 原主链入口。
- Workspace builders/ 拆分不改变主链，只改变内部对象转换组织。

# Confirmed Pipeline

输入：
- WorkspaceSnapshot。

输出：
- ConfirmedOrderObject。

内部组织：
- build_confirmed_order_object 仍是 Confirmed Pipeline 原主链入口。
- Confirmed builders/ 拆分不改变主链，只改变内部对象转换组织。

# Export Strategy Pipeline

事实链：
- WorkspaceSnapshot → ConfirmedOrderObject → ExportStrategy。
- ConfirmedOrderObject 承载人工修正和补齐后的最终填写事实。
- ExportStrategy 不得直接读取 WorkspaceSnapshot。

输入：
- ConfirmedOrderObject。

步骤：
- 读取最终事实（Final Truth）。
- ConfirmedField → ExportOperation(write_value)。
- ConfirmedTable → ExportOperation(write_table)。
- ConfirmedImage → ExportOperation(insert_image)。
- 生成 ExportStrategy。
- 生成 ExportOperation。
- 校验导出可执行性。

输出：
- ExportStrategy。
- ExportOperation。

内部组织：
- build_export_strategy 仍是 ExportStrategy Pipeline 主入口。
- operations/ 拆分只改变内部组织，不改变主链。
- 当前支持 ConfirmedField → write_value。
- 当前支持 ConfirmedTable → write_table。
- 当前支持 ConfirmedImage → insert_image。
- insert_image 当前属于导出计划，不代表真实图片写入已完成。

禁止：
- 不直接写文件。
- 不绕过 ConfirmedOrderObject。
- 不直接读取 WorkspaceSnapshot。

# Choice 链路设计

设计链路：

ChoiceCandidate
↓
ChoiceNode
↓
WorkspaceChoice
↓
ConfirmedChoice
↓
ExportStrategy

当前接入状态：
- ChoiceCandidate → ChoiceNode 已支持 `choice_mode` 与 `option_details`。
- ChoiceNode → WorkspaceChoice 已支持 `choice_mode`、`option_details` 与 `selected_values`。
- WorkspaceChoice → ConfirmedChoice 已传播 `choice_mode`、`option_details`、`selected_values` 与 `final_selected_values`。
- ConfirmedChoice → ExportOperation(set_choice) 已接入。
- ConfirmedChoice → ExportOperation(set_choice) → Excel Executor 已打通。

Choice 中层链路：

ChoiceNode
↓
WorkspaceChoice
↓
ConfirmedChoice
↓
ExportStrategy

职责转换：
- ChoiceNode → WorkspaceChoice：将模板事实转换为可确认结构。
- WorkspaceChoice → ConfirmedChoice：将可确认结构转换为人工确认后的最终事实。
- ConfirmedChoice → ExportStrategy：生成独立 `set_choice` 计划，并保留 `choice_mode` 供 Executor 后续解释。

不同 `choice_mode` 的导出策略方向：
- Choice 当前统一生成 `set_choice` 导出计划。
- `set_choice.value` 同时承载 `final_value` 与 `final_selected_values`，供后续 Executor 按 `choice_mode` 解释。

边界：
- Excel Executor 已实现第一版 `set_choice` 坐标型勾选。
- Word / PDF Executor 尚未实现 `set_choice`。
- Condition 不在本次 Choice Core 设计中处理。

# Condition Policy 链路

ConditionCandidate
↓
ConditionNode
↓
WorkspaceCondition
↓
ConfirmedCondition
↓
ExportPolicy
↓
ExportStrategy

职责转换：
- ConditionCandidate → ConditionNode：将条件候选转换为模板规则事实。
- ConditionNode → WorkspaceCondition：将模板规则转换为可确认的中层表达。
- WorkspaceCondition → ConfirmedCondition：形成确认后的规则事实。
- ConfirmedCondition → ExportPolicy：计算规则对导出计划的影响。
- ExportPolicy → ExportStrategy：决定相关导出动作应生成、保留或跳过。

边界：
- Condition 不直接生成 ExportOperation。
- Condition 不进入 `app/export/operations/`。
- ConditionPolicy 位于 `app/export/policies/`。
- ConditionPolicy V1 已支持 `export` 与 `skip_export`。
- ConditionPolicy 使用 ConfirmedField / ConfirmedChoice 最终事实解析 `source_field`。
- 条件无法判断时记录 warning，并保守跳过受控节点。

# Export Execute Pipeline

输入：
- ExportStrategy。

步骤：
- 读取 ExportOperation。
- 选择 Executor。
- 调用对应文档类型的 Executor。
- 生成最终输出文件。

当前执行器支持：
- Excel Executor：write_value、write_table、insert_image 占位校验、set_choice 第一版。
- Word Executor：docx placeholder 替换。
- PDF Executor：基础执行入口和 skipped 结果。

输出：
- Excel、PDF 或 Word 输出文件。

禁止：
- 不生成 ExportStrategy。
- 不绕过 ExportStrategy 直接读取 ConfirmedOrderObject。
- 不自行判断字段目标位置。
# Template Analysis Reality Gap

`STAGE3_REALITY_VALIDATION_RUN_01` 暴露的断点位于：

Template Reader
↓
Template Analysis
↓
Detector 层

而不是：

DocumentModel / Workspace / Confirmed / ExportStrategy / Executor。

说明：
- 当前真实验证中 Template Reader 能读取真实 Excel 模板。
- Template Analysis 只产出 Table，未产出 Field、Choice、Condition、Image。
- DocumentModel、Workspace、Confirmed 和 ExportStrategy 均能消费现有 TemplateAnalysisResult。
- Excel Executor 的 `write_table` / `start_cell` 契约问题属于后续执行层契约对齐，不是本轮 Template Analysis 首要断点。

后续目标链：

Excel Template
↓
Excel Reader
↓
Field Detector
↓
Choice Detector
↓
Condition Detector
↓
Image Detector
↓
Table Detector
↓
TemplateAnalysisResult
↓
DocumentModel

升级原则：
- Pipeline 只组织流程。
- Detector 负责识别能力。
- Pipeline 已完成不等于 Detection 已完成。
