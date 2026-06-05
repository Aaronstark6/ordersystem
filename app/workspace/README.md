目录：app/workspace

职责：承载用户确认工作区模型和构建逻辑。

输入：DocumentModel、匹配结果和人工确认数据。

输出：供用户确认或修正的工作区结构。

上游：Workspace Pipeline、DocumentModel、Matching Pipeline。

下游：Human Confirm Pipeline、Export Strategy Pipeline。

禁止：不读取模板，不执行导出，不保存第二套事实。
