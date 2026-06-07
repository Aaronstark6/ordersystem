# 当前任务

# 当前任务

当前任务：
- STAGE3_WORKSPACE_NODE_INTEGRATION_01。

目标：
- 将 TableNode 接入 WorkspaceSnapshot。
- 将 ImageNode 接入 WorkspaceSnapshot。
- 将 ChoiceNode 接入 WorkspaceSnapshot。
- 将 ConditionNode 接入 WorkspaceSnapshot。
- 保持现有 FieldNode / SectionNode 接线。

边界：
- 只处理 DocumentModel → WorkspaceSnapshot。
- Workspace 是中层表达层，不是页面。
- 不修改 Core、Routes、UI、Executor 或 Export。
