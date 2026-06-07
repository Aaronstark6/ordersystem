# 当前任务

当前任务：
- STAGE3_IMAGE_EXPORT_INTEGRATION_01。

目标：
- 补齐 ConfirmedImage → ExportOperation(insert_image)。
- Section 与未分区图片都进入 ExportStrategy。
- 保持 Field / Table 现有导出计划不变。
- 本任务不处理 Choice / Condition。

边界：
- insert_image 只表示导出计划。
- 不读取图片文件，不执行真实图片写入。
- 不修改 Core、DocumentModel、Workspace、Confirmed、Routes、UI 或 Executor。
