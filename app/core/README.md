目录：app/core

职责：系统能力层，只提供能力，不组织流程。

输入：文件、数据契约、DocumentModel 或 Pipeline 传入的原始数据。

输出：结构化分析结果、候选结果或能力函数返回值。

上游：Workflow、Routes 的未来调用入口。

下游：Contracts、DocumentModel。

禁止：不写 Pipeline，不写 Route，不写 UI，不保存状态，不直接操作 Storage。
