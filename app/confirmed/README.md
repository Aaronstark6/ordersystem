目录：
app/confirmed

职责：
负责把工作区快照（WorkspaceSnapshot）中用户确认后的内容转换为人工确认对象（ConfirmedOrderObject）。

输入：
工作区快照（WorkspaceSnapshot）。
用户修改值（User Values）。

输出：
人工确认对象（ConfirmedOrderObject）。
确认字段（ConfirmedField）。
确认区域（ConfirmedSection）。

上游：
工作区（Workspace）。

下游：
导出策略（ExportStrategy）。

禁止：
不读取 Excel。
不分析模板。
不生成工作区。
不直接写 Excel。
不直接生成导出策略。
不保存状态。
不写页面。
不写路由业务。

关键规则：
ConfirmedOrderObject 是导出前的最终事实（Final Truth）。
ExportStrategy 必须读取 ConfirmedOrderObject，不能绕过人工确认直接读取 WorkspaceSnapshot。
