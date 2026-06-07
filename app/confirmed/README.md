目录：
app/confirmed

职责：
ConfirmedOrderObject 是人工确认后的最终填写事实层。
它以 WorkspaceSnapshot 为基础，承载人工修正和补齐后的最终内容。
它用于修正 AI 错误内容、补齐 AI 缺失内容。

输入：
工作区快照（WorkspaceSnapshot）。
用户修改值（User Values）。

输出：
人工确认对象（ConfirmedOrderObject）。
确认字段（ConfirmedField）。
确认表格（ConfirmedTable）。
确认图片（ConfirmedImage）。
确认选择（ConfirmedChoice）。
确认条件（ConfirmedCondition）。
确认区域（ConfirmedSection）。

上游：
工作区（Workspace）。

下游：
导出策略（ExportStrategy）。

Builder 组织：
- builder.py 是 build_confirmed_order_object 总调度入口。
- builders/ 目录承载 Workspace 对象到 Confirmed 对象的具体转换器。
- field_builder.py 负责 ConfirmedField。
- table_builder.py 负责 ConfirmedTable。
- image_builder.py 负责 ConfirmedImage。
- choice_builder.py 负责 ConfirmedChoice。
- condition_builder.py 负责 ConfirmedCondition。
- 未来新增对象类型时，应新增独立 builder 文件，不应继续堆入 builder.py。

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
ConfirmedOrderObject 是 ExportStrategy 的唯一输入事实来源。
ExportStrategy 必须读取 ConfirmedOrderObject，不能绕过人工确认直接读取 WorkspaceSnapshot。
