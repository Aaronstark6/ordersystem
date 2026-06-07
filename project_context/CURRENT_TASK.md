# 当前任务

当前任务：
- STAGE3_EXPORT_STRATEGY_TABLE_INTEGRATION_01。

目标：
- 补齐 ConfirmedTable → ExportOperation(write_table)。
- 保留 ConfirmedField → ExportOperation(write_value)。
- Section 和未分区表格都进入 ExportStrategy。
- 本任务不处理 Image、Choice、Condition。

边界：
- ExportStrategy 只生成写入计划，不直接写文件。
- 不修改 Core、DocumentModel、Workspace、Confirmed、Routes、UI 或 Executor。
