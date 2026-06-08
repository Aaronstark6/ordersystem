# 当前任务

当前任务：
- `STAGE3_STORAGE_STRUCTURE_AND_LAYER_01`

目标：
- 创建 `data/` 标准目录与 `app/storage/` 最小路径管理层。

边界：
- 只新增 Storage V1 最小能力。
- 不修改主链业务代码。
- 不把业务逻辑写入 `app/storage/`。
- 不把 `audit_output/` 纳入系统 Storage。
- 不修改主链或任何代码逻辑。
# 当前任务更新

当前任务：
- `STAGE3_TEMPLATE_ANALYSIS_REBUILD_PLAN_01`

目标：
- 记录 Template Analysis 真实断点与后续 detector 升级路线。
- 明确 Field / Choice / Condition / Image / Table Detector 当前真实能力、缺口、拆分边界和后续升级顺序。

边界：
- 只修改 `project_context/` 文档。
- 不修改 `app/**`。
- 不新增代码文件。
- 不修改 `data/**`。
- 不修改 `.gitignore`。
- 不直接重写 Template Analysis。
- 不把所有 detector 逻辑塞进 `analyzer.py`。
