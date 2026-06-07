系统目标：
订单资料 -> 理解模板 -> DocumentModel -> Workspace -> 人工确认 -> ExportStrategy -> Excel/PDF/Word。

当前第一版只做 Excel 闭环。

分层边界：
- Core：能力层，只提供能力。
- DocumentModel：统一事实中心。
- Contracts：跨层数据契约。
- Workflow：流程组织。
- Workspace：用户确认工作区。
- Export：导出策略和操作模型。
- Storage：读写持久化。
- State：状态推进。
- Routes：接口入口。
- UI：页面展示。
- Diagnostics：诊断。

禁止规则：
- 页面不写业务。
- 路由不写业务。
- Storage 不做业务判断。
- State 不保存第二套事实。

Storage / Cache / Runtime Boundary：
- 系统运行产生的持久化文件只能写入 `data/`。
- `app/` 只存放代码，禁止写入运行文件、缓存、导出结果和日志。
- `project_context/` 只存放项目文档，禁止写入运行文件、缓存和导出结果。
- 仓库根目录禁止生成运行文件、缓存、导出结果和日志。
- `data/templates/` 长期保存正式模板；小型非敏感样本模板可按需进入 Git，真实业务大模板默认不进入 Git。
- `data/uploads/` 保存用户上传的临时文件，可清理，默认不进入 Git。
- `data/runtime/` 保存当前模板分析结果、Workspace、Confirmed 等运行中间状态，可清理，默认不进入 Git。
- `data/cache/` 保存可重新生成的模板分析、AI 解析和匹配缓存，可清理，默认不进入 Git。
- `data/exports/` 保存导出结果，可清理或归档，默认不进入 Git。
- `data/samples/` 保存小型测试样本和验证模板，可长期保留并允许进入 Git，但必须控制大小和敏感性。
- `audit_output/` 是开发审计临时目录，不属于系统运行存储体系，不参与系统架构设计，由 Owner 定期手动清理。
- 未来 `app/storage/` 只负责路径管理、授权目录创建、清理策略和文件命名，不做业务判断。
- 业务模块不得自行拼接持久化路径；任何 `open(..., "w")`、`save`、`export`、`mkdir` 或缓存写入逻辑必须遵守 Storage 规则。
- 未确认写入归属时不得落盘。

坐标标准（Coordinate Standard）：
- Coordinate 是系统唯一坐标模型和标准坐标来源。
- 当前 Coordinate 支持 Excel / PDF / Word 三类表达。
- 禁止创建 CoordinateV2、PdfCoordinate、WordCoordinate、VisualCoordinate。
- Workspace、ExportStrategy、未来 Pipeline 禁止直接依赖 cell、range_ref、source_cell、target_cell。
- 上游原始坐标必须先转换为 Coordinate，再进入下游。

工作区（Workspace）层：
- Workspace 负责把 DocumentModel 转换成人可以查看、编辑、确认的数据结构。
- Workspace 是中层表达层，不是页面，页面只展示 Workspace。
- Workspace 不负责导出。
- Workspace 不负责状态推进。
- Workspace 不负责模板分析。

人工确认对象（ConfirmedOrderObject）层：
- ConfirmedOrderObject 是人工确认后的最终填写事实层，不是 Workspace 的简单复制。
- ConfirmedOrderObject 用于修正 AI 错误、补齐 AI 缺失内容。
- ConfirmedOrderObject 形成最终写入 Excel / Word / PDF 的事实对象。
- ConfirmedOrderObject 位于 Workspace 之后、ExportStrategy 之前。
- 导出链路不得绕过 ConfirmedOrderObject。

中层 Builder 组织：
- Workspace 与 Confirmed 都属于中层（Middle Layer）。
- 各层 builder.py 只负责总调度和对象归属组装。
- 具体对象转换逻辑进入各自 builders/ 子目录。
- 禁止把所有对象转换继续堆入一个巨型 builder.py。

当前已建立：
- Workspace Builders。
- Confirmed Builders。
- Export Operations。

提前拆分属于架构策略，不是功能需求。
其目标是保持职责清晰并预防持续增长的 Builder 巨文件化。

导出策略（ExportStrategy）层：
- ExportStrategy 负责把 ConfirmedOrderObject 转换为 ExportOperation。
- ExportStrategy builder.py 只负责总调度。
- ExportOperation 具体构建逻辑进入 app/export/operations。
- ExportStrategy 内部已分为 `operations/` 与 `policies/`。
- `operations/` 负责生成导出动作。
- `policies/` 负责根据规则影响导出动作的生成。
- Condition 属于 policy，不属于 operation。
- `app/export/policies/` 已开始由 ConditionPolicy V1 承担导出规则策略。
- 禁止把具体操作构建继续堆入巨型 Export builder.py。
- ExportStrategy 当前支持字段、表格、图片和选择导出计划。
- 字段导出计划来自 ConfirmedField。
- 表格导出计划来自 ConfirmedTable。
- 图片导出计划来自 ConfirmedImage，并转换为 ExportOperation(insert_image)。
- 选择导出计划来自 ConfirmedChoice，并转换为 ExportOperation(set_choice)。
- ConditionPolicy V1 通过 export/skip_export 影响上述导出计划是否生成。
- ExportStrategy 只生成写入计划，不直接写 Excel / PDF / Word 文件。
- ConfirmedOrderObject 不得绕过 ExportStrategy 直接进入 Executor。

# 当前开发阶段

## 阶段一（Stage 1）

最小主链（Minimum Main Chain）

状态：
- 已完成。
- 已验证通过。

完成链路：

Excel 模板
↓
TemplateAnalysisResult
↓
DocumentModel
↓
WorkspaceSnapshot
↓
ConfirmedOrderObject
↓
ExportStrategy
↓
ExportOperation
↓
Excel Executor
↓
最终 Excel 文件

# 新开发路线

## 阶段二（Stage 2）

内核完善（Core Completion）

## 阶段三（Stage 3）

中层整合（Middle Layer Integration / Workspace Integration）

## 阶段四（Stage 4）

配置页（Config）

## 阶段五（Stage 5）

外层入口（Routes / UI）

## 阶段六（Stage 6）

订单解析（AI Parser）与匹配（Matching）

## 后续

PDF / Word
