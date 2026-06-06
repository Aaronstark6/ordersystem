# AI Order System / OrderSystem 协作规则

## 项目角色

- Owner
- ChatGPT
- Codex
- Solo
- PowerShell
- Git

## 职责边界

Owner：
- 负责产品目标。
- 负责最终决策。
- 不直接编写代码。

ChatGPT：
- 负责架构。
- 负责审计分析。
- 负责根因定位。
- 负责路线规划。
- 负责任务拆解。
- 负责生成 Codex / Solo 指令。
- 不直接修改仓库。

Codex：
- 负责代码修改。
- 严格执行任务。
- 不自由重构。
- 不自由扩展范围。

Solo：
- 负责机械执行。
- 复制。
- 粘贴。
- 删除。
- 搜索。
- 运行命令。
- 不负责架构设计。

PowerShell：
- 默认审计工具。
- 负责真实状态采集。
- 审计输出目录：`D:\CursorFilses\ordersystem\audit_output`。

Git：
- 负责版本管理。
- 负责 Tag 管理。
- 负责里程碑管理。

## 审计规则

- 审计优先使用 PowerShell。
- 先审计，后修改。
- 禁止凭记忆开发。
- 必须以真实代码为依据。
- 复杂审计输出到 `audit_output`。
- 复杂审计结果打包为 ZIP，回传 ChatGPT 分析。

## 修改规则

- ChatGPT 是大脑。
- Codex / Solo 是手。
- 不允许自由发挥。
- 不允许自行重构。
- 不允许扩大修改范围。
- 必须严格执行任务要求。

## Git 规则

- 重要节点必须打 Tag。

当前：
- `CORE_COMPLETION_V1`

后续：
- `WORKSPACE_V1`
- `CONFIG_CENTER_V1`
- `AI_RUNTIME_V1`
- `BETA_V1`

## 新聊天页对齐规则

新聊天开始先阅读：
- `ARCHITECTURE.md`
- `ARCHITECTURE_RULES.md`
- `CORE_CAPABILITIES.md`
- `DOCUMENT_MODEL.md`
- `PIPELINES.md`
- `FILE_TREE.md`
- `PROJECT_STATUS.md`
- `CURRENT_TASK.md`
- `CURRENT_PLAN.md`
- `COLLABORATION_RULES.md`

然后执行：

```powershell
git status
git log --oneline --decorate -20
```

确认真实状态后再继续任务。
