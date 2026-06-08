# Export Operations

职责：
- operations/ 负责把 ConfirmedOrderObject 中的不同确认对象转换为 ExportOperation。

当前已有：
- value_operation.py：ConfirmedField → write_value。
- table_operation.py：ConfirmedTable → write_table。
- image_operation.py：ConfirmedImage → insert_image。
- choice_operation.py：ConfirmedChoice → set_choice。

未来扩展：
- condition_policy.py：ConfirmedCondition 参与策略生成，不直接生成导出操作。

图片边界：
- 当前不处理真实图片文件。
- 当前不调用 Executor。

选择边界：
- set_choice 当前只生成导出计划。
- 当前不调用 Executor。
- 当前不执行真实勾选。

禁止：
- 不直接执行导出。
- 不调用 Executor。
- 不读取模板文件。
- 不写文件。
- 不处理 Routes / UI。
# Table Export Contract V1

`table_operation.py` is responsible for converting `ConfirmedTable` into an executor-ready `write_table` operation.

Contract gap fixed in `STAGE3_TABLE_EXPORT_CONTRACT_FIX_01`:
- Before: `write_table.target` carried Coordinate fields such as `row`, `column`, `width`, and `height`, but did not include `start_cell`.
- Before: `write_table.value` was a descriptive dict containing `headers`, `row_count`, and `column_count`.
- Excel Executor expects `target["start_cell"]` and `value` as a list of rows.

Current contract:
- `target["sheet_name"]` comes from the existing Coordinate.
- `target["start_cell"]` is derived from existing Coordinate `cell`, or from `row` + `column`.
- `value` is a `list[list]`.
- The first row contains table headers.
- Remaining rows are blank placeholders based on current `row_count`.
- Original descriptive table data is preserved in operation metadata.

Boundary:
- This operation builder does not read Excel files.
- This operation builder does not execute exports.
- This operation builder does not create a second table coordinate model.
- Complex table filling remains a future capability.
