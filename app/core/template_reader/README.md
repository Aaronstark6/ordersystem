目录：
app/core/template_reader

职责：
提供模板读取能力（Template Reader）。

当前能力：
- Excel 真实读取。
- PDF 基础识别。
- Word 基础识别。
- 统一模板读取入口（Template Reader Dispatcher）。

输入：
- 模板文件路径。

输出：
- Excel 工作表读取结果。
- PdfTemplateInfo。
- WordTemplateInfo。

上游：
- 模板接收流程（Template Intake）。

下游：
- 模板分析（Template Analysis）。

当前不做：
- 不深度解析 PDF 内容。
- 不深度解析 Word 内容。
- 不生成文档模型（DocumentModel）。
- 不生成工作区（Workspace）。
- 不执行导出（Export）。

禁止：
- 不组织 Pipeline。
- 不写页面（UI）。
- 不写路由（Routes）。
- 不保存状态（State）。
