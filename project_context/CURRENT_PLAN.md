当前阶段：P0 新系统骨架初始化。

当前目标：只建立目录边界，不实现业务。

第一版闭环：Excel 模板上传、模板分析、DocumentModel、Workspace、人工确认、ExportStrategy、Excel 导出。

暂不做：PDF、Word、多用户、权限、复杂任务队列、高级诊断页面。

P0-2 DocumentModel 类型骨架：
已建立 Coordinate、FieldNode、TableNode、ImageNode、ChoiceNode、ConditionNode、SectionNode、Relationship、ValidationIssue、DocumentModel。
当前 DocumentModel 只定义统一事实结构，不负责识别、不负责导出、不负责流程。
