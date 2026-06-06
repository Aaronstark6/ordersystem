DocumentModel 是唯一事实中心。

# CORE_COMPLETION_V1

以下文档模型能力已进入 `CORE_COMPLETION_V1`：
- Coordinate。
- FieldNode。
- TableNode。
- SectionNode。
- ImageNode。
- ConditionNode。
- ChoiceNode。

接入状态：
- Image Logic 已接入 DocumentModel。
- Condition Logic 已接入 DocumentModel。
- Choice Logic 已接入 DocumentModel。

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
- 当前支持：FieldNode、TableNode、SectionNode、ImageNode、ConditionNode、ChoiceNode。
- 成功生成的 DocumentModel 至少包含一个节点。
- 所有生成节点统一使用 Coordinate。

待验证设计点：
- Relationship 是否需要独立存在。
- 保留至：DOCUMENTMODEL_RELATIONSHIP_AUDIT_01。

# 节点接入状态

ImageNode：
- ImageNode 是 DocumentModel 中表达图片区域、图片占位区、图片上传位置的节点。
- 当前已通过 TemplateAnalysisResult.images 接入 DocumentModel Builder。

ConditionNode：
- ConditionNode 描述“谁控制谁”。
- 条件来源可以是产品类型等字段。
- 被控制对象可以是软糖区域、胶囊区域、图片区域等节点。
- 当前已通过 TemplateAnalysisResult.conditions 接入 DocumentModel Builder。

ChoiceNode：
- ChoiceNode 表达单选、多选、互斥选项和默认选项。
- 当前已通过 TemplateAnalysisResult.choices 接入 DocumentModel Builder。

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

# TemplateAnalysisResult 契约

模板分析结果契约已扩展，当前可承载：
- field_labels。
- tables。
- visual_regions。
- images。
- conditions。
- choices。

Image、Condition、Choice 通过 TemplateAnalysisResult 中的
images、conditions、choices 进入 DocumentModel。
