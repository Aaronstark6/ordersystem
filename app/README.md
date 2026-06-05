目录：app

职责：承载 AI Order System 新系统应用代码。

输入：来自 Routes、Workflow、Core、Storage、State 等层的模块组织。

输出：可被应用入口、测试和未来服务调用的系统模块。

上游：project_context。

下游：app 下各分层目录。

禁止：不在根目录直接堆放业务逻辑。
