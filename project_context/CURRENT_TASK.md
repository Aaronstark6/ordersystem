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
# 当前任务：Field Target Cell Pipeline Fix

当前任务：
- `STAGE3_FIELD_TARGET_CELL_PIPELINE_FIX_01`

目标：
- 打通 Field Detector 到 ExportStrategy 的 `target_cell` 主链。
- 追踪并修复 `metadata["target_cell"]` 从 TemplateAnalysisResult 进入 DocumentModel、Workspace、Confirmed、ExportStrategy 的丢失点。

边界：
- 只修 `target_cell` 传递。
- 不修改 Choice / Condition / Image / Table。
- 不修改 Storage。
- 不修改 Excel Executor。
- 不新增第二套坐标模型。
- 保持小步修改。

# 当前任务：Field Detection Reality Upgrade

当前任务：
- `STAGE3_FIELD_DETECTION_REALITY_UPGRADE_01`

目标：
- 升级 Field Detector V1。
- 让真实 Excel 模板至少能识别基础字段标签。
- 推断或预留最小 `target_cell`。

边界：
- 只修改 Field Logic 与必要文档。
- 不修改 `app/core/template_analysis/analyzer.py`。
- 不修改 Choice / Condition / Image / Table。
- 不修改 DocumentModel / Workspace / Confirmed / Export / Executor。
- 不新增复杂规则引擎。
- 当前 `field_detector.py` 保持小文件，不拆分。

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
# 当前任务：Table Export Contract Fix

当前任务：
- `STAGE3_TABLE_EXPORT_CONTRACT_FIX_01`

目标：
- 修复 `write_table` operation 与 Excel Executor 的契约不一致。
- 只解决 `write_table`。

边界：
- 不修改 Choice / Condition / Image / Field。
- 不修改 Storage。
- 不修改 Excel Reader。
- 不修改 Excel Executor。
- 不新增第二套 table 坐标模型。
- 保持小步修改。

Contract Gap：
- `write_table.target` 缺少 `start_cell`。
- `write_table.value` 不是 Executor 所需的 row-list。
# 当前任务：Choice Detection V1

当前任务：
- `STAGE3_CHOICE_DETECTION_V1_01`

目标：
- 实现 Choice Detection V1。
- 让真实模板首次产生 `choice_count > 0` 与 `set_choice > 0`。

边界：
- 只实现 Choice Detection。
- 不修改 Field / Table / Condition / Image。
- 不修改 DocumentModel / Workspace / Confirmed / ExportStrategy / Executor。
- 不新增复杂规则引擎。
# 当前任务：Table Merged Cell Write Guard

当前任务：
- `STAGE3_TABLE_MERGED_CELL_WRITE_GUARD_01`

目标：
- 修复 Excel Executor 执行 `write_table` 时遇到 merged cell 的 read-only 报错。
- 命中 openpyxl `MergedCell` 时优先写入所属合并区域左上角。
- 无法安全定位合并区域时跳过该单元格并记录 warning。

边界：
- 只修改 Excel Executor 的 table 写入保护。
- 不修改 Field / Choice / Condition / Image / Template Analysis / ExportStrategy。
- 不修改 table operation contract。
# 当前任务：Image Detection V1

当前任务：
- `STAGE3_IMAGE_DETECTION_V1_01`

目标：
- 实现 Image Detection V1。
- 让真实模板首次产生 `image_count > 0` 并进入现有 Image 主链。

边界：
- 只修改 Image Logic 与 analyzer 接入。
- 不修改 Field / Choice / Table / Condition。
- 不修改 DocumentModel / Workspace / Confirmed / Export / Executor。
- 不处理真实图片文件、嵌入图片对象、图片尺寸或复杂锚点。
# 当前任务：Table Detection Guardrail

当前任务：
- `STAGE3_TABLE_DETECTION_GUARDRAIL_01`

目标：
- 收紧 Table Detector V1。
- 减少普通字段布局、choice、image placeholder 和 validation/control mapping 行被误判为 table。

边界：
- 只修改 Table Logic。
- 不修改 Field / Choice / Image / Condition。
- 不修改 DocumentModel / Workspace / Confirmed / ExportStrategy / Executor。
- 不修改 table export contract。
# 当前任务：Condition Detection V1

当前任务：
- `STAGE3_CONDITION_DETECTION_V1_01`

目标：
- 实现 Condition Detection V1。
- 让真实模板首次产生 `condition_count > 0` 并进入现有 Condition Pipeline。

边界：
- 只修改 Condition Logic 与 analyzer 接入。
- 不修改 Field / Choice / Table / Image。
- 不修改 DocumentModel / Workspace / Confirmed / ExportStrategy / Executor。
