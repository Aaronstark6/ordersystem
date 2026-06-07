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
- `STAGE3_CONDITION_POLICY_IMPLEMENTATION_01`

当前状态：
- 正在实现 ConditionPolicy V1。
- ConfirmedCondition 可在 operation 生成前通过 export/skip_export 影响 ExportStrategy。
- Condition 本身仍不生成 ExportOperation，Executor 保持不变。
