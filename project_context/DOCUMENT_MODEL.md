DocumentModel 是唯一事实中心。

当前已建立：
- Coordinate。
- FieldNode。
- TableNode。
- ImageNode。
- ChoiceNode。
- ConditionNode。
- SectionNode。
- Relationship。
- ValidationIssue。
- DocumentModel。

当前规则：
- DocumentModel 不负责识别。
- DocumentModel 不负责导出。
- DocumentModel 不负责流程。
- DocumentModel 只描述系统看到的文档世界。

当前已建立：
- TemplateAnalysisResult 到 DocumentModel 的第一版构建链。

DocumentModel Builder：
- 转换来源：TemplateAnalysisResult。
- 当前支持：FieldNode、TableNode、SectionNode。
- 成功生成的 DocumentModel 至少包含一个节点。
- 所有生成节点统一使用 Coordinate。

待验证设计点：
- Relationship 是否需要独立存在。
- 保留至：DOCUMENTMODEL_RELATIONSHIP_AUDIT_01。

# 待新增节点

- ConditionNode。
- ChoiceNode。
- ImageNode。

# DocumentModel V1 冻结条件

以下节点全部完成并验证通过：
- FieldNode。
- TableNode。
- SectionNode。
- ConditionNode。
- ChoiceNode。
- ImageNode。
