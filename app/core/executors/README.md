目录：
app/core/executors

职责：
提供导出执行能力（Executor Capabilities）。

当前能力：
- Excel 执行器（Excel Executor）。
- Word 执行器（Word Executor）。
- PDF 执行器（PDF Executor）基础入口。
- write_value。
- write_table。
- insert_image 占位校验。
- 导出操作结果（ExportOperationResult）。
- Excel 导出结果（ExcelExportResult）。
- 通用导出执行结果（ExportExecutionResult）。
- 成功、跳过、失败操作统计。

输入：
Excel 模板文件路径。
输出文件路径。
导出策略（ExportStrategy）。
导出操作（ExportOperation）。

输出：
- 最终 Excel 文件。
- ExcelExportResult。

上游：
导出策略（ExportStrategy）。

下游：
文件下载（Download）。
导出记录（Export Record）。

禁止：
不生成导出策略。
不修改人工确认对象（ConfirmedOrderObject）。
不修改工作区快照（WorkspaceSnapshot）。
不分析模板。
不生成文档模型（DocumentModel）。
不写页面（UI）。
不写路由业务（Routes）。
不保存状态（State）。

关键规则：
执行器（Executor）只执行导出操作（ExportOperation）。
执行器（Executor）不得自己决定字段写到哪里。
字段写入目标必须来自导出策略（ExportStrategy）。

当前不做：
- 不真正插入图片。
- 不自行决定写入位置。

样式原则：
执行器只写单元格值，不主动修改模板样式。

Word Executor：
- 支持 docx placeholder 替换。
- 当前不支持复杂表格写入。
- 当前不支持 bookmark 真实定位。
- 不修改原 Word 模板。

PDF Executor：
- 当前只提供执行入口和 skipped 结果。
- 不真实写 PDF。
- 输出文件为原 PDF 模板副本。
- 后续支持 AcroForm 或坐标覆盖写入。
