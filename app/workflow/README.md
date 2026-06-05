目录：app/workflow

职责：只组织 Pipeline。

输入：Routes 或任务入口传入的请求数据和中间结果。

输出：按步骤推进后的流程结果。

上游：Routes、State。

下游：Core、DocumentModel、Workspace、Export、Storage、State。

禁止：不实现核心能力，不直接写页面，不直接做存储细节。
