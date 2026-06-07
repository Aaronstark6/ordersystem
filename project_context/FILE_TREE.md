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
- 中层工作区表达层，不是页面。
- model.py：定义 WorkspaceSnapshot、WorkspaceSection、WorkspaceField、WorkspaceTable、WorkspaceImage、WorkspaceChoice、WorkspaceCondition。
- builder.py：DocumentModel 转换为 WorkspaceSnapshot 的总调度入口。
- builders/field_builder.py：FieldNode 转换为 WorkspaceField。
- builders/table_builder.py：TableNode 转换为 WorkspaceTable。
- builders/image_builder.py：ImageNode 转换为 WorkspaceImage。
- builders/choice_builder.py：ChoiceNode 转换为 WorkspaceChoice。
- builders/condition_builder.py：ConditionNode 转换为 WorkspaceCondition。
- validators.py：校验 WorkspaceSnapshot 标识和可确认内容。
- serializer.py：将 WorkspaceSnapshot 转换为 dict。

app/confirmed：
- 人工确认后的最终填写事实层。
- model.py：定义 ConfirmedField、ConfirmedTable、ConfirmedImage、ConfirmedChoice、ConfirmedCondition、ConfirmedSection、ConfirmedOrderObject。
- builder.py：WorkspaceSnapshot 转换为 ConfirmedOrderObject 的总调度入口。
- builders/field_builder.py：WorkspaceField 转换为 ConfirmedField。
- builders/table_builder.py：WorkspaceTable 转换为 ConfirmedTable。
- builders/image_builder.py：WorkspaceImage 转换为 ConfirmedImage。
- builders/choice_builder.py：WorkspaceChoice 转换为 ConfirmedChoice。
- builders/condition_builder.py：WorkspaceCondition 转换为 ConfirmedCondition。
- validators.py：校验 ConfirmedOrderObject 标识和可确认对象。
- serializer.py：将 ConfirmedOrderObject 转换为 dict。
- README.md：说明人工确认层职责和边界。

app/export：
- 导出策略层。
- model.py：定义 ExportStrategy 和 ExportOperation。
- builder.py：ExportStrategy 总调度入口。
- operations/value_operation.py：ConfirmedField 转换为 write_value。
- operations/table_operation.py：ConfirmedTable 转换为 write_table。
- operations/image_operation.py：ConfirmedImage 转换为 insert_image。
- operations/README.md：说明操作构建器职责、扩展位和禁止边界。
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

app/core/table_logic：
- 表格逻辑（Table Logic）能力层。
- table_detector.py：识别表格候选并定义 TableRangeCandidate。
- header_detector.py：识别 TableHeaderCandidate。
- merged_cell_detector.py：将合并区域转换为 MergedCellCandidate。
- README.md：说明表格逻辑职责、当前能力和边界。

app/core/visual_logic：
- 视觉逻辑（Visual Logic）能力层。
- visual_region_detector.py：定义 VisualRegionCandidate 和 LayoutRegionCandidate。
- anchor_detector.py：定义 AnchorCandidate。
- coordinate_model.py：复用 Coordinate 并定义 CoordinateGroup。
- README.md：说明唯一坐标原则和禁止的第二套坐标类型。

app/core/field_logic：
- 字段逻辑（Field Logic）能力层。
- field_detector.py：识别字段标签并定义 FieldCandidate。
- field_normalizer.py：将字段标签标准化为字段 key。
- field_matcher.py：定义 FieldMatchCandidate 和简单字段匹配。
- README.md：说明字段逻辑职责、当前能力和边界。

app/core/ai_parser：
- 订单解析器内核（AI Parser Core）能力层。
- order_object.py：定义 OrderObject、OrderField、MissingField 和 ParseResult。
- order_parser.py：提供本地订单文本解析占位器。
- prompt_builder.py：构建未来 AI 解析使用的提示词。
- README.md：说明解析器内核能力和禁止边界。

app/core/matching：
- 匹配内核（Matching Core）能力层。
- match_result.py：定义 CandidateFillObject 和 CandidateFillField。
- confidence_scorer.py：提供简单字段匹配评分。
- semantic_matcher.py：把 OrderObject 与 DocumentModel 字段进行第一版匹配。
- README.md：说明匹配内核职责、当前能力和禁止边界。

app/core/executors：
- 导出执行能力层。
- 当前包含 Excel、Word、PDF 执行器及导出结果对象。
- excel_executor.py：执行 ExportStrategy 操作并生成 ExcelExportResult。
- result_model.py：定义通用 ExportExecutionResult 和 ExportOperationResult。
- word_executor.py：执行 docx placeholder 替换。
- pdf_executor.py：提供 PDF 基础执行入口和 skipped 结果。
- README.md：说明执行器能力、结果统计和禁止边界。

app/core/template_reader：
- 模板读取能力层。
- excel_reader.py：真实读取 Excel 工作表、单元格、合并区域和尺寸信息。
- pdf_reader.py：识别 PDF 模板文件并返回 PdfTemplateInfo。
- word_reader.py：识别 Word 模板文件并返回 WordTemplateInfo。
- reader_dispatcher.py：根据文件后缀调用对应模板读取器。
- README.md：说明模板读取能力和当前边界。
