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
