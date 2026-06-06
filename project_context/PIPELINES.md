当前 Pipeline 尚未实现。

计划主链：
- Template Intake Pipeline。
- Template Analysis Pipeline。
- DocumentModel Pipeline。
- Order Parse Pipeline。
- Matching Pipeline。
- Workspace Pipeline。
- Human Confirm Pipeline。
- Export Strategy Pipeline。
- Export Execute Pipeline。

当前原则：
- Pipeline 只组织流程。
- Pipeline 不实现核心能力。
- Pipeline 不直接写页面。
- Pipeline 不直接做存储细节。

Export Strategy Pipeline 计划：

输入：
- ConfirmedOrderObject。

步骤：
- 读取最终事实（Final Truth）。
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

Export Execute Pipeline 计划：

输入：
- ExportStrategy。

步骤：
- 读取 ExportOperation。
- 选择 Executor。
- 调用 Excel Executor。
- 生成最终 Excel 文件。

当前执行器支持：
- Excel Executor：write_value、write_table、insert_image 占位校验。
- Word Executor：docx placeholder 替换。
- PDF Executor：基础执行入口和 skipped 结果。

输出：
- 最终 Excel 文件。

禁止：
- 不生成 ExportStrategy。
- 不绕过 ExportStrategy 直接读取 ConfirmedOrderObject。
- 不自行判断字段目标位置。

# Stage 2 说明

Stage 2 期间优先完善 Core。

Workspace Pipeline 暂不继续扩展。

Config Pipeline 暂不继续扩展。
