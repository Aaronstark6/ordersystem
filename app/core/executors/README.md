目录：
app/core/executors

职责：
提供导出执行能力（Executor Capabilities）。

当前能力：
Excel 执行器（Excel Executor）。

输入：
Excel 模板文件路径。
输出文件路径。
导出策略（ExportStrategy）。
导出操作（ExportOperation）。

输出：
最终 Excel 文件。

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
