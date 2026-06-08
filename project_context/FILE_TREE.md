目录说明：
- app/core：系统能力层。
- app/contracts：跨层数据契约。
- app/document_model：统一事实中心。
- app/workflow：主链流程组织。
- app/workspace：工作区模型和构建。
- app/export：导出策略和操作模型。
- app/storage：基础设施层路径管理。
- app/state：状态记录和推进。
- app/routes：接口层。
- app/diagnostics：诊断层。
- app/ui：界面层。
- project_context：项目上下文和架构文档。

运行文件目录：
- `data/`：系统运行文件的唯一根目录；按数据职责和生命周期划分子目录。
- `data/templates/`：长期保存正式模板；小型非敏感样本模板可按需进入 Git，真实业务大模板默认不进入 Git。
- `data/uploads/`：用户上传的临时文件；可清理，默认不进入 Git。
- `data/runtime/`：当前模板分析结果、Workspace、Confirmed 等运行中间状态；可清理，默认不进入 Git。
- `data/cache/`：可重新生成的模板分析缓存、AI 解析缓存和匹配缓存；可清理，默认不进入 Git。
- `data/exports/`：导出结果；可清理或归档，默认不进入 Git。
- `data/samples/`：小型测试样本、验证模板和订单样本；可长期保留，允许进入 Git，但必须控制大小和敏感性。
- `audit_output/`：开发审计临时目录；不属于系统运行存储体系，不参与系统架构设计，由 Owner 定期手动清理。
- `app/`、`project_context/` 与仓库根目录不属于运行文件目录，禁止写入缓存、日志、临时文件或导出结果。
- 清理前必须核验解析后的绝对路径、目录用途和活动任务占用情况。
- 本目录规范描述授权边界，不要求预先创建尚不存在的 `data/` 子目录。

app/storage：
- paths.py：定义仓库根目录、`data/` 根目录和六个标准子目录路径常量。
- manager.py：提供授权目录创建、目录读取函数和安全路径解析。
- __init__.py：导出 Storage V1 最小公开函数。
- README.md：说明 Storage Layer 职责、边界和目录策略。
- 不做业务判断，不保存第二套业务事实。
- 业务模块不得绕过 Storage 规则自行拼接路径写文件。

data/ Git 策略：
- `data/templates/.gitkeep` 可进入 Git，用于保留正式模板目录；真实大模板后续按大小和敏感性决定是否提交。
- `data/samples/.gitkeep` 可进入 Git，用于保留小型样本目录；小型非敏感样本允许进入 Git。
- `data/uploads/.gitignore` 可进入 Git；目录内容默认不进入 Git。
- `data/runtime/.gitignore` 可进入 Git；目录内容默认不进入 Git。
- `data/cache/.gitignore` 可进入 Git；目录内容默认不进入 Git。
- `data/exports/.gitignore` 可进入 Git；目录内容默认不进入 Git。

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
- operations/choice_operation.py：ConfirmedChoice 转换为 set_choice。
- operations/README.md：说明操作构建器职责、扩展位和禁止边界。
- policies/：导出策略规则目录。
- policies/condition_policy.py：根据 ConfirmedCondition 的 export/skip_export 规则影响导出动作生成。
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
# Template Analysis / Detector 文件职责

当前真实文件：
- `app/core/template_analysis/analyzer.py`
- `app/core/field_logic/field_detector.py`
- `app/core/field_logic/field_normalizer.py`
- `app/core/field_logic/field_matcher.py`
- `app/core/choice_logic/choice_detector.py`
- `app/core/choice_logic/choice_resolver.py`
- `app/core/condition_logic/condition_detector.py`
- `app/core/condition_logic/condition_evaluator.py`
- `app/core/image_logic/image_detector.py`
- `app/core/image_logic/image_anchor.py`
- `app/core/table_logic/table_detector.py`
- `app/core/table_logic/header_detector.py`
- `app/core/table_logic/merged_cell_detector.py`

`analyzer.py` 职责：
- 调用各 detector。
- 汇总 `TemplateAnalysisResult`。
- 记录 warnings / errors / metadata。

`analyzer.py` 禁止：
- 写具体字段识别规则。
- 写具体 choice 识别规则。
- 写具体 condition 识别规则。
- 写具体 image 识别规则。
- 写具体 table 边界识别规则。

`field_logic/` 后续升级：
- `field_detector.py` 保持轻量。
- 可在需要时新增 `label_patterns.py` 或等价小文件，用于中英文标签、冒号字段、相邻空白目标格等规则。

`choice_logic/` 后续升级：
- `choice_detector.py` 可继续保留 ChoiceCandidate / ChoiceOption / ChoiceGroup 的结构能力。
- 如识别逻辑增长，再评估拆出 `checkbox_detector.py`、`dropdown_detector.py` 或 `patterns.py`。
- 不要一开始过度拆分；超过约 200 到 300 行再评估。

`condition_logic/` 后续升级：
- `condition_detector.py` 负责最小条件候选识别。
- 可按真实业务增长拆出 `condition_patterns.py` 或 `condition_rule_parser.py`。
- 第一版只聚焦 `equals` / `skip_export` 等最小规则识别。

`image_logic/` 后续升级：
- `image_detector.py` 负责图片区域候选。
- 后续可按真实复杂度新增 `image_area_detector.py`，但不得提前写成已存在文件。

`table_logic/` 后续升级：
- `table_detector.py` 负责表格候选主判断。
- 当前真实文件包含 `header_detector.py` 和 `merged_cell_detector.py`。
- 不得把不存在的 `header_detection.py` 或 `merged_cell_detection.py` 写成已存在。
- 后续重点是降低误判，避免普通布局行被吞成 table。
