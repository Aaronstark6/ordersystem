# app/core/field_logic

Field Logic provides the first-stage field detection capability for Template Analysis.

Current Field Detector V1:
- Detects common Chinese field labels.
- Detects common English field labels case-insensitively.
- Supports labels ending with English colon `:` or Chinese colon `：`.
- Trims whitespace around labels and colons before matching.
- Rejects empty values, pure numeric values, and overly long text.
- Infers a minimal adjacent `target_cell` when possible.

`target_cell` inference:
- Right adjacent blank cell is preferred, for example `A3` label and blank `B3` means `target_cell = B3`.
- Below adjacent blank cell is the fallback, for example `A3` label and blank `A4` means `target_cell = A4`.
- If neither adjacent cell is blank, `target_cell = None`.
- The current shared `FieldLabelCandidate` contract has no declared `target_cell` field, so V1 stores this as runtime `metadata["target_cell"]` on the candidate without changing contracts.

Current limits:
- Does not infer complex merged-cell targets.
- Does not search across regions.
- Does not inspect cells beyond one adjacent right or down cell.
- Does not detect Choice, Condition, Table, or Image objects.
- Does not generate DocumentModel, Workspace, Confirmed, Export, or Executor behavior.
