# Export Operations

职责：
- operations/ 负责把 ConfirmedOrderObject 中的不同确认对象转换为 ExportOperation。

当前已有：
- value_operation.py：ConfirmedField → write_value。
- table_operation.py：ConfirmedTable → write_table。
- image_operation.py：ConfirmedImage → insert_image。

未来扩展：
- choice_operation.py：ConfirmedChoice → write_value 或专用选择写入逻辑。
- condition_policy.py：ConfirmedCondition 参与策略生成，不直接生成导出操作。

图片边界：
- 当前不处理真实图片文件。
- 当前不调用 Executor。

禁止：
- 不直接执行导出。
- 不调用 Executor。
- 不读取模板文件。
- 不写文件。
- 不处理 Routes / UI。
