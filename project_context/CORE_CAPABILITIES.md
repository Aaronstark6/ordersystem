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
