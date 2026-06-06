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
- PDF 读取。
- Word 读取。
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
- 当前只支持 write_value 操作。
- 当前不支持 PDF / Word。

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
