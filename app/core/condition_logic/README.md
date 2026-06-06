目录：
app/core/condition_logic

职责：
提供条件逻辑（Condition Logic）能力。

当前能力：
- ConditionCandidate。
- ConditionRule。
- ConditionEvaluator。

支持：
- equals。
- not_equals。

当前不支持：
- 复杂表达式。
- AND。
- OR。
- 嵌套条件。

边界：
- 候选构建函数只负责结构化输入。
- Evaluator 只读取传入字段值并计算布尔结果。
- 不修改 Workspace、ConfirmedOrderObject、ExportStrategy 或 Executor。
