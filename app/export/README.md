目录：app/export

职责：承载导出策略和操作模型。

输入：DocumentModel、Workspace 确认结果和导出目标信息。

输出：ExportStrategy 和导出操作描述。

上游：Export Strategy Pipeline。

下游：Export Execute Pipeline。

禁止：当前不实现 Excel/PDF/Word 导出执行，不写 Route，不写 UI。
