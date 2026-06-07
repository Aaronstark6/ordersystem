1. 页面不能组织业务。
2. 路由不能写业务。
3. Pipeline 只能组织流程。
4. Core 只提供能力。
5. DocumentModel 是唯一事实中心。
6. State 只记录状态，不保存第二套事实。
7. Storage 只负责读写，不做业务判断。
8. 新增功能优先判断是否只是现有 Pipeline 的一个 Step。
9. 不清楚归属的功能，先不写。
10. 第一版宁可功能少，也不能边界乱。

# 架构铁律（Architecture Laws）

DocumentModel 是事实层，只表达文档事实。

允许进入 DocumentModel：
- FieldNode。
- TableNode。
- SectionNode。
- ImageNode。
- ChoiceNode。
- ConditionNode。
- Coordinate。
- Relationship。

禁止进入 DocumentModel：
- Workspace 状态。
- UI 状态。
- Config 状态。
- 导出状态。
- AI 状态。
- Prompt。
- 日志。
- Runtime 状态。
- 用户确认状态。

# 中层铁律（Middle Layer Laws）

- Workspace 负责组织事实，形成可确认的中层表达。
- Confirmed 负责保存人工确认后的最终填写事实。
- Export 负责生成导出计划。
- 各层不得跨层承担其他层的职责。
- Workspace 不得成为页面状态。
- Confirmed 不得承担导出执行。
- Export 不得绕过 Confirmed 读取 Workspace。

# Builder 铁律

builder.py 只负责：
- 总调度。
- 编排。
- 对象归属与主流程组装。

具体对象转换逻辑进入：
- builders/。

具体导出操作构建逻辑进入：
- operations/。

禁止把所有对象转换或操作构建逻辑堆入单个 builder.py。

# 巨文件预防规则

- 发现某类文件必然持续增长时，允许提前拆分。
- 不要等文件成为巨文件后再拆分。
- 文件达到约 200 至 300 行时，应评估职责是否需要拆分。
- 拆分必须保持公开入口、数据结构和业务行为稳定。

# 新对象扩展规则

未来新增以下对象时：
- Signature。
- Attachment。
- Barcode。
- QRCode。
- Stamp。

必须按完整链路扩展：

DocumentModel
↓
Workspace Builder
↓
Confirmed Builder
↓
Export Operation
↓
Executor

禁止跳层实现，禁止直接硬塞进现有对象转换逻辑。
