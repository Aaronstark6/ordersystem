# 当前任务

当前任务：
- STAGE3_CONFIRMED_OBJECT_NODE_INTEGRATION_01。

目标：
- 补齐 WorkspaceSnapshot → ConfirmedOrderObject。
- 承载 Field、Table、Image、Choice、Condition。
- 允许人工修正 Field 和 Choice。
- 保持 ConfirmedOrderObject 为 ExportStrategy 唯一事实输入。

边界：
- 只处理 WorkspaceSnapshot → ConfirmedOrderObject。
- 不修改 Core、DocumentModel、Workspace、Routes、UI、Executor 或 Export。
