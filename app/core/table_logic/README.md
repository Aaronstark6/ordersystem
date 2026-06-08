目录：
app/core/table_logic

职责：
提供表格逻辑（Table Logic）能力。

当前能力：
- 表格候选识别（Table Candidate Detection）。
- 表头候选识别（Header Candidate Detection）。
- 合并单元格识别（Merged Cell Detection）。
- 表格范围候选（TableRangeCandidate）。
- Table Detector Guardrail V1。
- 排除明显字段布局行、choice 行、image placeholder 行和 validation/control mapping 行。
- 表格候选必须具备表头证据，并且存在数据行或明确 table 标题。

当前不做：
- 不生成 DocumentModel。
- 不生成 Workspace。
- 不执行 Export。
- 不写 UI。
- 不写 Routes。
- 不做复杂表格引擎。
- 不修改 table export contract。
