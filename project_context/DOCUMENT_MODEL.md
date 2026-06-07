DocumentModel 是唯一事实中心。

# DocumentModel 边界规则

DocumentModel 只表达文档事实。

允许内容：
- FieldNode。
- TableNode。
- SectionNode。
- ImageNode。
- ChoiceNode。
- ConditionNode。
- Coordinate。
- Relationship。

禁止内容：
- Workspace、UI、Config 状态。
- 导出、AI、Runtime 状态。
- Prompt、日志。
- 用户确认状态。

完整边界规则以 `ARCHITECTURE_RULES.md` 为准。

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

# ChoiceNode 设计说明

当前 ChoiceNode 保存：
- `choice_key`。
- `options: List[str]`。
- `allow_multiple`。
- `default_option`。
- `choice_mode`。
- `option_details: List[dict]`。

当前兼容规则：
- `options: List[str]` 暂时保留，用于旧链路兼容。
- `option_details` 承载 structured options。
- `option_details` 可保存 option coordinate、模板声明的 selected state 和 option metadata。

边界：
- ChoiceNode 仍属于文档事实层。
- ChoiceNode 可以保存模板中有哪些选择项，以及每个选项在哪里。
- ChoiceNode 不保存用户确认结果。
- 用户最终选择结果属于 ConfirmedChoice。

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
