目录说明：
- app/core：系统能力层。
- app/contracts：跨层数据契约。
- app/document_model：统一事实中心。
- app/workflow：主链流程组织。
- app/workspace：工作区模型和构建。
- app/export：导出策略和操作模型。
- app/storage：持久化读写。
- app/state：状态记录和推进。
- app/routes：接口层。
- app/diagnostics：诊断层。
- app/ui：界面层。
- project_context：项目上下文和架构文档。

app/workspace：
- 工作区层。
- model.py：定义 WorkspaceSnapshot、WorkspaceSection、WorkspaceField。
- builder.py：把 DocumentModel 转换为 WorkspaceSnapshot。
- validators.py：校验 WorkspaceSnapshot。
- serializer.py：将 WorkspaceSnapshot 转换为 dict。

app/confirmed：
- 人工确认层。
- model.py：定义 ConfirmedOrderObject、ConfirmedSection、ConfirmedField。
- builder.py：把 WorkspaceSnapshot 转换为 ConfirmedOrderObject。
- validators.py：校验 ConfirmedOrderObject。
- serializer.py：将 ConfirmedOrderObject 转换为 dict。
- README.md：说明人工确认层职责和边界。

app/export：
- 导出策略层。
- model.py：定义 ExportStrategy 和 ExportOperation。
- builder.py：把 ConfirmedOrderObject 转换为 ExportStrategy。
- validators.py：校验 ExportStrategy。
- serializer.py：将 ExportStrategy 转换为 dict。
- README.md：说明导出策略层职责和边界。

app/core/image_logic：
- 图片逻辑（Image Logic）能力层。
- image_detector.py：定义 ImageAreaCandidate 和结构化构建函数。
- image_anchor.py：定义 ImageAnchorCandidate 和结构化构建函数。
- README.md：说明图片逻辑职责和边界。

app/core/condition_logic：
- 条件逻辑（Condition Logic）能力层。
- condition_detector.py：定义 ConditionCandidate 和结构化构建函数。
- condition_evaluator.py：定义 ConditionRule 和 ConditionEvaluator。
- README.md：说明条件逻辑职责、支持范围和边界。

app/core/choice_logic：
- 选择逻辑（Choice Logic）能力层。
- choice_detector.py：定义 ChoiceCandidate、ChoiceOption 和 ChoiceGroup。
- choice_resolver.py：校验并解析单选或多选结果。
- README.md：说明选择逻辑职责、支持范围和边界。
