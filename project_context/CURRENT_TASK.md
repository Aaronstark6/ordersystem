# 当前任务

当前任务：
- `STAGE3_CHOICE_DOCUMENTMODEL_UPGRADE_01`

目标：
- 将 Choice Contract 新能力传播到 ChoiceNode。
- 保留旧 options 字符串链路，同时承载 choice_mode 与 option_details。

边界：
- 只升级 ChoiceNode 与 DocumentModel Builder。
- 不修改主链。
- 不向 Workspace、Confirmed、Export 或 Executor 传播。
