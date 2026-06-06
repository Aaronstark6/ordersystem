目录：
app/workspace

职责：
负责把文档模型（DocumentModel）转换为用户可确认的工作区快照（WorkspaceSnapshot）。

输入：
文档模型（DocumentModel）。

输出：
工作区快照（WorkspaceSnapshot）。
工作区区域（WorkspaceSection）。
工作区字段（WorkspaceField）。

上游：
文档模型构建器（DocumentModel Builder）。

下游：
人工确认链（Human Confirm Pipeline）。
未来页面（UI）。

禁止：
不读取 Excel。
不分析模板。
不调用 AI。
不写导出文件。
不直接保存状态。
不写路由业务。
