# app/storage

Storage Layer 是 OrderSystem 的基础设施层，不属于主链。

职责：
- 提供 `data/` 标准目录的统一路径定义。
- 提供授权目录创建能力。
- 提供最小路径解析能力。

边界：
- Storage 不理解 DocumentModel、Workspace、ConfirmedOrderObject、ExportStrategy 或 Executor 等业务对象。
- Storage 不做业务判断，不组织流程，不保存第二套事实。
- 业务模块禁止直接拼接 `data/` 路径。
- 业务模块未来应通过 Storage Layer 获取持久化路径。

目录策略：
- `data/templates/` 可长期保留，用于正式模板。
- `data/samples/` 可长期保留，用于小型测试样本和真实验证。
- `data/uploads/` 可清理，用于上传文件。
- `data/runtime/` 可清理，用于运行时状态。
- `data/cache/` 可清理，用于可重新生成的缓存。
- `data/exports/` 可清理或归档，用于导出结果。

非 Storage：
- `audit_output/` 是开发审计临时目录，不属于系统 Storage。
