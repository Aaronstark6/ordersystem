目录：
app/workspace

职责：
负责把文档模型（DocumentModel）转换为用户可确认的工作区快照（WorkspaceSnapshot）。
Workspace 是中层表达层，不是页面。

输入：
文档模型（DocumentModel）。

输出：
工作区快照（WorkspaceSnapshot）。
工作区区域（WorkspaceSection）。
工作区字段（WorkspaceField）。
工作区表格（WorkspaceTable）。
工作区图片（WorkspaceImage）。
工作区选择（WorkspaceChoice）。
工作区条件（WorkspaceCondition）。

上游：
文档模型构建器（DocumentModel Builder）。

下游：
人工确认链（Human Confirm Pipeline）。
未来页面（UI）。

Builder 组织：
- builder.py 是 build_workspace_snapshot 总调度入口。
- builders/ 目录承载具体 DocumentModel 节点到 Workspace 对象的转换器。
- field_builder.py 负责 WorkspaceField。
- table_builder.py 负责 WorkspaceTable。
- image_builder.py 负责 WorkspaceImage。
- choice_builder.py 负责 WorkspaceChoice。
- condition_builder.py 负责 WorkspaceCondition。
- 未来新增 Signature、Attachment、Barcode 等对象时，应新增独立 builder 文件，不应继续堆入 builder.py。

禁止：
不读取 Excel。
不分析模板。
不调用 AI。
不写导出文件。
不直接保存状态。
不写路由业务。
不组织页面展示。
