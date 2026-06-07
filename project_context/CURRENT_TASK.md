# 当前任务

当前任务：
- `STAGE3_CHOICE_CONTRACT_UPGRADE_01`

目标：
- 升级 ChoiceOption / ChoiceCandidate 契约承载能力。
- 让 Choice Core 能记录 option coordinate 和 choice_mode。

边界：
- 只升级 Choice Core 的前端契约承载。
- 不修改主链。
- 不向 DocumentModel、Workspace、Confirmed、Export 或 Executor 传播。
- 不新增 checkbox、radio 或 dropdown 自动识别。
