# 当前任务

当前任务：
- `STAGE3_STORAGE_CACHE_RUNTIME_DESIGN_01`

目标：
- 设计存储、缓存、运行时、导出和样本目录体系。
- 明确 `data/` 子目录职责、Git 策略、清理策略及 Pipeline 读写边界。
- 明确 `audit_output/` 只是开发审计临时目录，不属于系统运行存储体系。

边界：
- 只修改 `project_context/` 文档。
- 不修改 `app/`、`data/`、`audit_output/` 或 `.gitignore`。
- 不创建 `data/` 子目录。
- 不修改主链或任何代码逻辑。
