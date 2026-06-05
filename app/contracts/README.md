目录：app/contracts

职责：定义跨层数据契约。

输入：各层需要共享的数据结构需求。

输出：跨 Core、Workflow、DocumentModel、Workspace、Export 使用的数据结构。

上游：Core、Workflow、DocumentModel。

下游：所有需要稳定数据形状的层。

禁止：不实现业务逻辑，不负责流程，不读写文件。
