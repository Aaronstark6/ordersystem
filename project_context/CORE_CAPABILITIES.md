当前已建立：
- Excel Template Core。

已具备：
- 读取 Excel 工作表。
- 提取非空或有样式单元格。
- 识别合并单元格信息。
- 读取行高列宽。
- 识别字段标签候选。
- 识别基础表格候选。
- 生成基础视觉区域。
- 输出 TemplateAnalysisResult。

当前未实现：
- PDF 深度解析。
- Word 深度解析。
- AI 订单解析。
- 匹配能力。
- 条件逻辑。
- 选择逻辑。
- 导出执行。

Core 禁止：
- 不写 Pipeline。
- 不写 Route。
- 不写 UI。
- 不保存状态。
- 不直接操作 Storage。

Excel Template Core 修正：
合并单元格识别已从字符串匹配改为真实坐标范围判断。
避免 A1 与 A10 等坐标误判问题。

导出执行能力（Executor Capability）：
- 当前已建立 Excel 执行器（Excel Executor）。
- 支持根据 ExportStrategy 中的 ExportOperation 把值写回 Excel 模板。
- 当前不支持 PDF / Word。

导出执行增强（Executor Enhancement）：

当前能力：
- Excel 执行器（Excel Executor）。
- write_value。
- write_table。
- insert_image 占位校验。
- ExcelExportResult。
- 操作结果统计。

当前未实现：
- Excel 真正图片插入。

PDF / Word 执行器（PDF / Word Executor）：

当前能力：
- Word Executor 支持 docx placeholder 替换。
- PDF Executor 支持基础执行入口和结果记录。
- 通用 ExportExecutionResult。
- 通用 ExportOperationResult。

当前未实现：
- PDF 真实写入。
- Word 复杂表格写入。
- Word bookmark 真实定位。
- 图片真实插入 PDF / Word。

# Stage 2 Core Completion

待完成能力：

图片逻辑（Image Logic）：

当前能力：
- 定义图片区域候选（ImageAreaCandidate）。
- 定义图片锚点候选（ImageAnchorCandidate）。
- 为后续 Template Analysis 和 DocumentModel 接入图片能力做准备。

当前未实现：
- 不读取真实图片文件。
- 不插入图片。
- 不执行图片导出。

条件逻辑（Condition Logic）：

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

选择逻辑（Choice Logic）：

当前能力：
- ChoiceCandidate。
- ChoiceOption。
- ChoiceGroup。
- ChoiceResolver。
- 单选校验。
- 多选支持。
- 非法选项拒绝。

当前未实现：
- 自动识别选择区域。
- 与 Condition Logic 自动联动。
- 接入 Workspace。
- 接入 ExportStrategy。

表格逻辑增强（Table Logic Enhancement）：

当前能力：
- 表格候选识别（Table Candidate Detection）。
- 表头候选识别（Header Candidate Detection）。
- 合并单元格识别（Merged Cell Detection）。
- 表格范围候选（TableRangeCandidate）。

当前未实现：
- 表格数据自动填充。
- 与 DocumentModel Builder 的完整接入。
- 高级跨行跨列表格判断。

视觉逻辑增强（Visual Logic Enhancement）：

当前能力：
- Coordinate。
- CoordinateGroup。
- VisualRegionCandidate。
- LayoutRegionCandidate。
- AnchorCandidate。

唯一规则：
- Coordinate 是唯一坐标标准。
- 禁止建立第二套坐标体系。

统一坐标模型（Unified Coordinate Model）：
- Coordinate 已扩展支持 Excel / PDF / Word。
- Excel 使用单元格坐标。
- PDF 使用页面绝对坐标。
- Word 使用段落、表格、书签和占位符结构坐标。

字段逻辑增强（Field Logic Enhancement）：

当前能力：
- 字段候选（FieldCandidate）。
- 字段标准化（Field Normalization）。
- 字段匹配候选（FieldMatchCandidate）。
- 简单字段匹配（Simple Field Matching）。

当前未实现：
- AI 语义匹配。
- 与 AI Parser 完整接入。
- 与 DocumentModel Builder 完整接入。

订单解析器内核（AI Parser Core）：

当前能力：
- OrderObject。
- OrderField。
- MissingField。
- ParseResult。
- parse_order_text_stub。
- Prompt Builder。

当前未实现：
- 真实 AI 调用。
- API Key 管理。
- 多模型适配。
- 与 Matching 完整接入。

匹配内核（Matching Core）：

当前能力：
- 候选填充值对象（CandidateFillObject）。
- 候选填充字段（CandidateFillField）。
- 字段匹配评分（score_field_match）。
- OrderObject 到 DocumentModel 的字段匹配。

当前未实现：
- AI 语义匹配。
- 多候选排序。
- 人工映射配置。
- 表格数据匹配。
- 与 Workspace 的完整接入。

模板读取扩展（Template Reader Expansion）：

当前能力：
- Excel 模板真实读取。
- PDF 模板基础识别。
- Word 模板基础识别。
- 统一模板读取入口（Template Reader Dispatcher）。

当前未实现：
- PDF 内容深度解析。
- Word 内容深度解析。
- PDF / Word 模板分析。

Core 到 DocumentModel 的接入状态：
- Image Logic 已通过 TemplateAnalysisResult 接入 DocumentModel。
- Condition Logic 已通过 TemplateAnalysisResult 接入 DocumentModel。
- Choice Logic 已通过 TemplateAnalysisResult 接入 DocumentModel。
