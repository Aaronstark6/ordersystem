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
Condition Detection V1：
- 支持 if / IF / 如果 / 满足 / 当。
- 支持 equals / = / == / 等于。
- 支持 contains / 包含 / 包含关键词。
- 支持 export / skip export / 隐藏 / 显示 基础导出控制识别。
- 只生成 ConditionCandidate，不执行条件。

当前不支持：
- AND / OR。
- nested condition。
- 复杂表达式。
