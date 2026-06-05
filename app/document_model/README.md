目录：app/document_model

职责：定义 DocumentModel 统一事实中心。

输入：未来由 TemplateAnalysisResult 和订单解析结果构建出的统一事实。

输出：系统看到的文档世界结构。

上游：DocumentModel Pipeline、Core、Contracts。

下游：Workspace、Matching、Export Strategy。

禁止：不负责识别，不负责导出，不负责流程。
