# 项目状态

当前里程碑：
- `CORE_COMPLETION_V1`

里程碑状态：
- 已完成。

已完成：
- Stage1 Minimum Main Chain。
- Stage2 Core Completion。
- STAGE3_MIDDLE_LAYER_BUILDER_SPLIT_01。
- STAGE3_EXPORT_OPERATION_ARCHITECTURE_PREPARE_01。
- STAGE3_ARCHITECTURE_RULES_HARDENING_01。
- STAGE3_IMAGE_EXPORT_INTEGRATION_01。

当前开发重点：
- Stage3 Middle Layer Integration。

当前任务：
- `STAGE3_STORAGE_STRUCTURE_AND_LAYER_01`

当前状态：
- Storage V1 已落地为基础设施层。
- 已创建 `data/` 标准目录结构。
- 已新增 `app/storage/` 最小路径管理层。
- 系统运行写入统一进入 `data/`；`audit_output/` 仅作为开发审计临时目录。
# Field Target Cell Pipeline Fix 状态

当前任务：
- `STAGE3_FIELD_TARGET_CELL_PIPELINE_FIX_01`

当前状态：
- 已定位 `target_cell` 丢失点在 TemplateAnalysisResult 到 DocumentModel 的 FieldNode 构建阶段。
- Field Detector 产出的 `metadata["target_cell"]` 必须进入 DocumentModel FieldNode 坐标。
- Workspace、Confirmed、ExportStrategy 继续沿用同一字段坐标，不新增第二套坐标模型。
- 本任务只修 Field target_cell 传递，不修改 Choice / Condition / Image / Table / Storage / Excel Executor。

# Field Detection Reality Upgrade 状态

当前任务：
- `STAGE3_FIELD_DETECTION_REALITY_UPGRADE_01`

当前状态：
- Field Detector V1 已进入真实模板补强小步。
- 本小步只补强 Field Logic，不修改 Choice / Condition / Image / Table。
- 本小步不修改 DocumentModel / Workspace / Confirmed / Export / Executor。
- Field Detector 支持中英文标签、冒号标签和最小 `target_cell` metadata。

# Template Analysis Reality Gap 状态更新

当前任务：
- `STAGE3_TEMPLATE_ANALYSIS_REBUILD_PLAN_01`

当前阶段：
- Stage3 已进入 Template Analysis Reality Gap 修复阶段。
- 下游主链已验证出结构可用：DocumentModel、Workspace、Confirmed、ExportStrategy 和 Excel Executor 均可被真实链路调用。
- 当前优先级转向上游 detector 能力补齐。

真实验证暴露：
- Field = 0。
- Choice = 0。
- Condition = 0。
- Image = 0。
- Table = 13。
- ExportStrategy 只生成 `write_table`。
- 当前最大断点是 Template Analysis 未正确产出下游对象。
# Table Export Contract Fix 状态

当前任务：
- `STAGE3_TABLE_EXPORT_CONTRACT_FIX_01`

Contract Gap：
- ExportStrategy 生成的 `write_table` 缺少 Excel Executor 所需的 `target.start_cell`。
- ExportStrategy 生成的 `write_table.value` 是描述性 dict，不是 Excel Executor 所需的行列表。

当前状态：
- `write_table.target.start_cell` 从现有 Coordinate 推导。
- `write_table.value` 转为 `list[list]`。
- 原 headers / row_count / column_count 保留在 operation metadata。
- 未修改 Excel Executor。
- 未新增第二套 table 坐标模型。
# Choice Detection V1 状态

当前任务：
- `STAGE3_CHOICE_DETECTION_V1_01`

当前状态：
- Choice Pipeline 已存在，本小步补齐 Choice Detection V1。
- V1 只产出 ChoiceCandidate，不修改下游主链。
- 支持 Checkbox、Radio、Yes/No 与常见二选一。
- Dropdown、复杂 MultiSelect、跨区域复杂分组仍留后续。
# Table Merged Cell Write Guard 状态
当前任务：
- `STAGE3_TABLE_MERGED_CELL_WRITE_GUARD_01`

当前状态：
- RUN_03 已验证 `write_value 10/10` 与 `set_choice 1/1` 成功。
- `write_table` 剩余失败点为 Excel Executor 写入 merged cell 时触发 openpyxl read-only 异常。
- 本小步只在 Excel Executor 的 table 写入层增加 MergedCell 防护。
- 不修改 Field / Choice / Condition / Image / Template Analysis / ExportStrategy / table operation contract。
# Image Detection V1 状态
当前任务：
- `STAGE3_IMAGE_DETECTION_V1_01`

当前状态：
- Field / Choice / Table 已完成真实链路验证。
- 当前小步补齐 Image Detection V1，让真实模板产出 `image_count > 0`。
- Image Detector V1 只识别图片占位文字，并推断基础 `image_role`。
- 不修改 DocumentModel / Workspace / Confirmed / Export / Executor。
- 不处理真实图片插入、嵌入图片扫描、图片尺寸或复杂锚点。
# Table Detection Guardrail 状态
当前任务：
- `STAGE3_TABLE_DETECTION_GUARDRAIL_01`

当前状态：
- RUN_04 发现 Table Detector V1 识别范围过宽，可能覆盖 Field 写入结果。
- 当前小步只收紧 Table Detection，不修改 Field / Choice / Image / Condition。
- 已加入 guardrail，减少字段布局、choice、image placeholder 和 validation/control mapping 行误判。
- 目标是减少误判，不是增强复杂表格能力。
