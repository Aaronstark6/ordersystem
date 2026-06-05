当前阶段：P0 新系统骨架初始化。

当前目标：只建立目录边界，不实现业务。

第一版闭环：Excel 模板上传、模板分析、DocumentModel、Workspace、人工确认、ExportStrategy、Excel 导出。

暂不做：PDF、Word、多用户、权限、复杂任务队列、高级诊断页面。

P0-2 DocumentModel 类型骨架：
已建立 Coordinate、FieldNode、TableNode、ImageNode、ChoiceNode、ConditionNode、SectionNode、Relationship、ValidationIssue、DocumentModel。
当前 DocumentModel 只定义统一事实结构，不负责识别、不负责导出、不负责流程。

P0-3 Excel Template Core：
已建立第一版正式 Excel 模板核心能力。
当前能力包括：读取 Excel 工作表、提取非空或有样式单元格、识别合并单元格、读取行高列宽、识别字段标签候选、识别基础表格候选、生成基础视觉区域、输出 TemplateAnalysisResult。
本阶段只属于 Core 层，不包含 Pipeline、Route、UI、State、Storage、Export。

P0-4 文档体系：
建立 ARCHITECTURE、CORE_CAPABILITIES、DOCUMENT_MODEL、PIPELINES、FILE_TREE、PROJECT_STATUS、CURRENT_TASK、DEPRECATED。
建立重要目录 README。
后续所有代码任务必须同步判断是否需要更新对应文档。
