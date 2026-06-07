目录：
app/core/choice_logic

职责：
提供选择逻辑（Choice Logic）能力。

当前能力：
- ChoiceCandidate。
- ChoiceOption。
- ChoiceGroup。
- ChoiceResolver。

支持：
- 单选。
- 多选。
- 默认选项字段。
- 选项合法性校验。
- ChoiceCandidate 的 choice_mode 契约。
- ChoiceOption 的选项坐标承载。

当前契约状态：
- 当前仅完成 choice_mode 和 option coordinate 的契约承载。
- choice_mode 可记录 value、checkbox_group、radio_group、dropdown、multiselect。
- TemplateAnalysisResult 通过 choices 列表承载增强后的 ChoiceCandidate。

当前不支持：
- 复杂条件联动。
- 选项自动识别。
- checkbox、radio、dropdown 的自动识别。
- 选项与 Condition Logic 的自动连接。
- 页面交互。
- 导出执行。

输入：
- Template Analysis 得到的选择候选。
- 用户选择值。

输出：
- 解析后的 ChoiceGroup。

上游：
- Template Analysis。
- 未来 Field Logic。

下游：
- DocumentModel。
- Condition Logic。
- 未来 Workspace。

后续传播：
- DocumentModel。
- Workspace。
- Confirmed。
- Export。

禁止：
- 不写页面。
- 不写路由。
- 不保存状态。
- 不执行导出。
- 不修改 ConfirmedOrderObject。
