# 当前任务

当前任务：
- `STAGE3_CONDITION_POLICY_IMPLEMENTATION_01`

目标：
- 实现 ConditionPolicy V1。
- 让 ConfirmedCondition 在 operation 生成前执行 export/skip_export 策略。

边界：
- 只实现 ExportPolicy 与 ExportStrategy 接线。
- 不修改主链。
- 不处理 show/hide、enable/disable。
- 不修改 Executor。
- Condition 不直接生成 ExportOperation。
