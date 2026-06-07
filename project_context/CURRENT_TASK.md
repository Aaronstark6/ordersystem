# 当前任务

当前任务：
- STAGE3_MIDDLE_LAYER_BUILDER_SPLIT_01。

目标：
- 拆分 Workspace / Confirmed builder。
- 保持现有公开入口和行为不变。
- 具体对象转换进入 builders/ 子目录。
- 预防 builder.py 继续增长为巨型文件。

边界：
- 只调整中层内部组织结构。
- 不改变数据结构或业务能力。
- 不修改 Core、DocumentModel、Export、Routes、UI 或 Executor。
