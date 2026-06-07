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
- 生成 ExportStrategy。
- 生成 ExportOperation。
- 校验导出可执行性。

输出：
- ExportStrategy。
- ExportOperation。

禁止：
- 不直接写文件。
- 不绕过 ConfirmedOrderObject。
- 不直接读取 WorkspaceSnapshot。

# Export Execute Pipeline

输入：
- ExportStrategy。

步骤：
- 读取 ExportOperation。
- 选择 Executor。
- 调用对应文档类型的 Executor。
- 生成最终输出文件。

当前执行器支持：
- Excel Executor：write_value、write_table、insert_image 占位校验。
- Word Executor：docx placeholder 替换。
- PDF Executor：基础执行入口和 skipped 结果。

输出：
- Excel、PDF 或 Word 输出文件。

禁止：
- 不生成 ExportStrategy。
- 不绕过 ExportStrategy 直接读取 ConfirmedOrderObject。
- 不自行判断字段目标位置。
