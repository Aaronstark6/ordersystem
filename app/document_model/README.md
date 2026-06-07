目录：app/document_model

职责：定义 DocumentModel 统一事实中心。

输入：未来由 TemplateAnalysisResult 和订单解析结果构建出的统一事实。

输出：系统看到的文档世界结构。

上游：DocumentModel Pipeline、Core、Contracts。

下游：Workspace、Matching、Export Strategy。

禁止：不负责识别，不负责导出，不负责流程。

DocumentModel Builder：

职责：将 TemplateAnalysisResult 转换为 DocumentModel。

当前支持：FieldNode、TableNode、SectionNode。

坐标规则：所有生成节点必须拥有 Coordinate，原始单元格或范围信息不得绕过 Coordinate 直接进入下游。

ImageNode：

ImageNode 是 DocumentModel 中表达图片区域、图片占位区和图片上传位置的节点。

当前 Stage 2 只建立 Image Logic 内核准备，尚未接入 DocumentModel Builder。

ConditionNode：

ConditionNode 描述条件及其控制的节点，也就是“谁控制谁”。

当前 Stage 2 已建立 ConditionCandidate、ConditionRule 和 ConditionEvaluator，尚未接入 DocumentModel Builder。

ChoiceNode：

ChoiceNode 用于表达单选、多选、互斥选项和默认选项等选择结构。

当前已通过 DocumentModel Builder 接入 Choice Logic 契约。

ChoiceNode 当前兼容两层表达：
1. `options: List[str]`：保留旧链路兼容。
2. `option_details: List[dict]`：承载结构化选项信息。

ChoiceNode 保存的模板事实：
- 选项有哪些。
- 选项模式是什么。
- 选项在模板中的位置是什么。

ChoiceNode 不保存用户最终选择结果。
用户最终选择结果属于 ConfirmedChoice。
