目录：
app/core/table_logic

职责：
提供表格逻辑（Table Logic）能力。

当前能力：
- 表格候选识别（Table Candidate Detection）。
- 表头候选识别（Header Candidate Detection）。
- 合并单元格识别（Merged Cell Detection）。
- 表格范围候选（TableRangeCandidate）。

当前不做：
- 不生成 DocumentModel。
- 不生成 Workspace。
- 不执行 Export。
- 不写 UI。
- 不写 Routes。
