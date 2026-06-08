# 当前计划

已完成：
- Stage1 最小主链。
- Stage2 核心补全。

当前：
- Stage3 中层整合。

Stage3 当前步骤：
1. Architecture Rules Hardening。
2. Core Capability Review。
3. Choice Core Design。
4. Choice Contract Upgrade。
5. Choice DocumentModel Upgrade。
6. Choice Middle Layer Model Design。
7. Choice Workspace Upgrade。
8. Choice Confirmed Upgrade。
9. Choice Export Strategy Upgrade。
10. Choice Executor Upgrade。
11. Condition Policy Design。
12. Condition Policy Implementation。
13. Storage Policy Design。
14. Storage / Cache / Runtime Design。
15. Storage Structure and Layer。

后续：
- Stage4 配置中心。
- Stage5 外层入口。
- Stage6 AI Runtime。
# 当前小步：STAGE3_FIELD_TARGET_CELL_PIPELINE_FIX_01

Field Detection Reality Upgrade 后续小步：打通 `target_cell` 主链。

目标链路：
- Field Detector
- TemplateAnalysisResult
- DocumentModel FieldNode
- Workspace Field
- Confirmed Field
- ExportStrategy `write_value`

修复原则：
- `target_cell` 进入 FieldNode 后作为 Field 的目标坐标使用。
- 不新增第二套坐标模型。
- 不修改 Choice / Condition / Image / Table。
- 不修改 Excel Executor。

# 当前小步：STAGE3_FIELD_DETECTION_REALITY_UPGRADE_01

Field Detection Reality Upgrade 是 Template Analysis Reality Gap 修复路线的当前小步。

目标：
- 修复 Field Detector 中文 hint 乱码。
- 补充英文 label hint。
- 支持中英文冒号标签。
- 增加相邻右侧 / 下方空白格的最小 `target_cell` 推断。

完成后继续按路线推进：
- `STAGE3_CHOICE_DETECTION_V1_01`
- `STAGE3_TABLE_DETECTION_GUARDRAIL_01`
- `STAGE3_IMAGE_DETECTION_V1_01`
- `STAGE3_CONDITION_DETECTION_V1_01`
- `STAGE3_REALITY_VALIDATION_RUN_02`

# Template Analysis Reality Gap 修复路线

推荐顺序：

1. `STAGE3_FIELD_DETECTION_REALITY_UPGRADE_01`
   - 修复字段识别。
   - 支持中英文标签、冒号字段、相邻空白目标格。

2. `STAGE3_CHOICE_DETECTION_V1_01`
   - 实现 checkbox / radio / value choice 的最小识别。

3. `STAGE3_TABLE_DETECTION_GUARDRAIL_01`
   - 降低 table 误判。
   - 避免普通布局行被吞成 table。

4. `STAGE3_IMAGE_DETECTION_V1_01`
   - 识别图片占位区。

5. `STAGE3_CONDITION_DETECTION_V1_01`
   - 只实现常规 `equals` / `skip_export` 等最小规则识别。

6. `STAGE3_REALITY_VALIDATION_RUN_02`
   - 重新跑真实模板验证。

拆分原则：
- 不直接重写 Template Analysis。
- 不把所有 detector 逻辑塞进 `analyzer.py`。
- detector 保持小文件、小职责，超过约 200 到 300 行再评估拆分。
# 当前小步：STAGE3_TABLE_EXPORT_CONTRACT_FIX_01

目标：
- 修复 Table Export Contract。
- 让 `ConfirmedTable -> ExportOperation(write_table)` 生成 Excel Executor 可直接消费的 `target.start_cell` 与 row-list value。

边界：
- 不修改 Excel Executor。
- 不修改 Table Detector。
- 不新增复杂表格引擎。
- 不新增第二套 table 坐标模型。

后续：
- 本小步只解决 operation contract。
- 表格真实数据填充、复杂表头、误判 guardrail 后续单独处理。
# 当前小步：STAGE3_CHOICE_DETECTION_V1_01

目标：
- 实现 Choice Detection V1。
- 支持 Checkbox、Radio、Yes/No 和常见二选一。
- 复用现有 `ChoiceCandidate` / `ChoiceOption` / `choice_mode`。

边界：
- 不改下游主链。
- 不做 Dropdown。
- 不做复杂 MultiSelect。
- 不做 Choice 执行逻辑。
# 当前小步：STAGE3_TABLE_MERGED_CELL_WRITE_GUARD_01

目标：
- 在 Excel Executor 的 `write_table` 写入前识别 openpyxl `MergedCell`。
- 将 merged cell 写入重定向到所属合并区域左上角。
- 无法定位合并区域时跳过单元格并记录 warning。

边界：
- 不修改 table operation contract。
- 不修改 ExportStrategy / Table Detector。
- 不影响 `write_value` 和 `set_choice`。
