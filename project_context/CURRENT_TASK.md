# 当前任务

当前任务：
- `STAGE3_STORAGE_POLICY_DESIGN_01`

目标：
- 固化存储、缓存、运行时、导出和审计输出边界。
- 明确授权写入目录及长期保留、可清理策略。

边界：
- 只修改 `project_context/` 文档。
- 不修改 `app/`、`data/`、`audit_output/` 或 `.gitignore`。
- 不创建 `data/` 子目录。
- 不修改主链或任何代码逻辑。
