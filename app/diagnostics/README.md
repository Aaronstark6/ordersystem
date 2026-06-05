目录：app/diagnostics

职责：提供诊断层能力和诊断结果组织。

输入：系统状态、Pipeline 结果、Core 输出和错误信息。

输出：诊断信息。

上游：Workflow、State、Core。

下游：Routes、UI、日志或报告入口。

禁止：不改变业务事实，不推进流程，不执行导出。
