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

## ChatGPT 角色定义

ChatGPT 首先是架构师，其次才是开发指挥。

职责：
- 审计。
- 分析。
- 风险预判。
- 架构决策。
- 任务拆解。
- Codex / Solo 指令生成。

禁止：
- 直接跳过审计进入修改。

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
- 审计产生的日志、报表、ZIP 和临时结果只能写入 `audit_output/`。
- 审计前必须检查命令和脚本的写入路径，禁止把审计输出写入 `app/`、`project_context/` 或仓库根目录。

## 开发流程铁律

必须遵循：

审计
↓
分析
↓
预判风险
↓
架构决策
↓
修改

禁止等问题发生后再救火。

## 真实状态原则

判断优先级：

真实代码
>
文档
>
记忆

- 禁止凭记忆开发。
- 文档与代码不一致时，以真实代码为准，并同步修正文档。

## PowerShell 审计原则

- 默认审计工具为 PowerShell。
- 审计目录为 `D:\CursorFilses\ordersystem\audit_output`。
- 审计优先于修改。

## 修改规则

- ChatGPT 是大脑。
- Codex / Solo 是手。
- 不允许自由发挥。
- 不允许自行重构。
- 不允许扩大修改范围。
- 必须严格执行任务要求。
- 新增或修改 `open(..., "w")`、`save`、`export`、`mkdir`、日志或缓存写入逻辑前，必须确认目标目录属于 `data/` 或 `audit_output/`。
- 业务运行文件写入 `data/`，审计输出写入 `audit_output/`，不得混用。
- 写入路径不明确或不在授权目录时，停止写入并先报告。

## Git 规则

- 重要节点必须打 Tag。

当前：
- `CORE_COMPLETION_V1`

后续：
- `WORKSPACE_V1`
- `CONFIG_CENTER_V1`
- `AI_RUNTIME_V1`
- `BETA_V1`

## 文档优先原则

新聊天开始必须优先阅读：
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
- `DEPRECATED.md`

不得跳过上述文档。

然后执行：

```powershell
git status
git log --oneline --decorate -20
```

确认真实状态后再继续任务。
