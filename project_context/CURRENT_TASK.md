# 当前任务

当前任务：
- STAGE3_EXPORT_OPERATION_ARCHITECTURE_PREPARE_01。

目标：
- 拆分 ExportOperation 构建逻辑。
- 预留 operations/ 扩展位。
- 保持 build_export_strategy 公开入口和行为不变。
- 预防 app/export/builder.py 继续增长为巨型文件。

边界：
- 只调整 ExportStrategy 内部组织结构。
- 不改变 ExportStrategy / ExportOperation 数据结构。
- 不新增 operation_type 或业务能力。
