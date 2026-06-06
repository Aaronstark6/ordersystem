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

# 待完成节点接入

ImageNode：
- ImageNode 是 DocumentModel 中表达图片区域、图片占位区、图片上传位置的节点。
- 当前 Stage 2 只建立 Image Logic 内核准备。
- 后续再接入 DocumentModel Builder。

ConditionNode：
- ConditionNode 描述“谁控制谁”。
- 条件来源可以是产品类型等字段。
- 被控制对象可以是软糖区域、胶囊区域、图片区域等节点。
- 当前 Stage 2 已建立 Condition Logic 内核能力。
- 后续再接入 DocumentModel Builder。

ChoiceNode：
- ChoiceNode 表达单选、多选、互斥选项和默认选项。
- 当前 Choice Logic 内核已建立。
- 尚未接入 DocumentModel Builder。

# DocumentModel V1 冻结条件

以下节点全部完成并验证通过：
- FieldNode。
- TableNode。
- SectionNode。
- ConditionNode。
- ChoiceNode。
- ImageNode。

# 坐标待决问题更新

当前仍需验证：
- Coordinate 是否足以表达未来 PDF / Word。

系统约束：
- 禁止出现第二套坐标标准。
- Visual Logic 必须继续复用 DocumentModel Coordinate。

# Coordinate 字段说明

Coordinate 是系统唯一坐标模型。

Excel：
- sheet_name。
- cell。
- row。
- column。

PDF：
- page_index。
- x。
- y。
- width。
- height。

Word：
- paragraph_index。
- table_index。
- bookmark。
- placeholder。
