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

导出策略（ExportStrategy）层：
- ExportStrategy 负责把 ConfirmedOrderObject 转换为 ExportOperation。
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
