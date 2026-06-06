目录：
app/core/matching

职责：
提供匹配内核（Matching Core）能力。

当前能力：
- 候选填充值对象（CandidateFillObject）。
- 候选填充字段（CandidateFillField）。
- 字段匹配评分（score_field_match）。
- 语义匹配器占位能力（Semantic Matcher Placeholder）。

输入：
- 订单对象（OrderObject）。
- 文档模型（DocumentModel）。

输出：
- 候选填充值对象（CandidateFillObject）。

上游：
- 订单解析器内核（AI Parser Core）。
- 文档模型（DocumentModel）。

下游：
- 工作区预填充（Workspace Prefill）。
- 未来工作区构建器（Workspace Builder）。

当前支持：
- 字段 key 完全匹配。
- 字段 key 包含匹配。

当前不支持：
- 真实 AI 语义匹配。
- 向量匹配。
- 多候选排序。
- 人工映射配置。
- 复杂表格匹配。

禁止：
- 不调用 AI。
- 不修改文档模型（DocumentModel）。
- 不生成工作区（Workspace）。
- 不生成导出策略（ExportStrategy）。
- 不写页面（UI）。
- 不写路由（Routes）。
- 不保存状态（State）。
