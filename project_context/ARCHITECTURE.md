系统目标：
订单资料 -> 理解模板 -> DocumentModel -> Workspace -> 人工确认 -> ExportStrategy -> Excel/PDF/Word。

当前第一版只做 Excel 闭环。

分层边界：
- Core：能力层，只提供能力。
- DocumentModel：统一事实中心。
- Contracts：跨层数据契约。
- Workflow：流程组织。
- Workspace：用户确认工作区。
- Export：导出策略和操作模型。
- Storage：读写持久化。
- State：状态推进。
- Routes：接口入口。
- UI：页面展示。
- Diagnostics：诊断。

禁止规则：
- 页面不写业务。
- 路由不写业务。
- Storage 不做业务判断。
- State 不保存第二套事实。
