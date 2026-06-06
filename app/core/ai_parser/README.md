目录：
app/core/ai_parser

职责：
提供订单解析器内核（AI Parser Core）能力。

当前能力：
- 订单对象（OrderObject）。
- 订单字段（OrderField）。
- 缺失字段（MissingField）。
- 解析结果（ParseResult）。
- 订单文本解析占位器（parse_order_text_stub）。
- 提示词构建器（Prompt Builder）。

当前不做：
- 不调用真实 AI 服务。
- 不保存 API Key。
- 不写路由。
- 不写页面。
- 不接入 Workspace。
- 不接入 Matching。

输入：
- 客户订单文本。

输出：
- OrderObject。
- ParseResult。

上游：
- Order Input。

下游：
- Matching。
- Workspace Prefill。

禁止：
- 不读取模板。
- 不生成 DocumentModel。
- 不直接生成 ExportStrategy。
- 不直接写 Excel。
