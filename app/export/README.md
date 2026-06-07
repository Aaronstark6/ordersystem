目录：
app/export

职责：
ExportStrategy 负责把 ConfirmedOrderObject 的最终事实转换为可执行导出计划。

当前支持：
- ConfirmedField → write_value。
- ConfirmedTable → write_table。

Builder 组织：
- builder.py 是 build_export_strategy 总调度入口。
- operations/ 承载具体 ExportOperation 构建器。
- value_operation.py 负责 ConfirmedField → write_value。
- table_operation.py 负责 ConfirmedTable → write_table。
- 未来新增 operation_type 时应新增独立 operations 文件，不应继续堆入 builder.py。

输入：
人工确认对象（ConfirmedOrderObject）。

输出：
导出策略（ExportStrategy）。
导出操作（ExportOperation）。

上游：
人工确认对象（ConfirmedOrderObject）。

下游：
导出执行器（Executor）。
Excel 执行器（Excel Executor）。
未来 PDF 执行器（PDF Executor）。
未来 Word 执行器（Word Executor）。

禁止：
不读取 Excel。
不分析模板。
不生成文档模型。
不生成工作区。
不修改人工确认对象。
不直接写 Excel / PDF / Word 文件。
不写页面。
不写路由业务。
不保存状态。

关键规则：
ExportStrategy 只生成写入计划。
Executor 才真正写文件。
ConfirmedOrderObject 不能绕过 ExportStrategy 直接进入 Executor。
