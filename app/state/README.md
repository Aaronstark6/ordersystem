目录：app/state

职责：只记录流程状态和推进状态。

输入：Pipeline 执行过程中的状态变化。

输出：当前流程状态。

上游：Workflow。

下游：Routes、Workflow、Diagnostics。

禁止：不保存第二套事实，不做业务判断，不替代 DocumentModel。
