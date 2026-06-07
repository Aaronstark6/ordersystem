# 当前任务

当前任务：
- `STAGE3_CHOICE_EXPORT_STRATEGY_UPGRADE_01`

目标：
- ConfirmedChoice → ExportOperation(set_choice)。
- 生成独立选择类导出计划，不执行真实勾选。

边界：
- 只升级 ExportStrategy 层。
- 不修改主链。
- 不修改 Core、DocumentModel、Workspace、Confirmed 或 Executor。
