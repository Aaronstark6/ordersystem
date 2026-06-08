目录：
app/core/image_logic

职责：
提供图片逻辑（Image Logic）的基础结构化能力。

当前能力：
- 定义图片区域候选（ImageAreaCandidate）。
- 定义图片锚点候选（ImageAnchorCandidate）。
- 使用 Coordinate 表达候选区域和锚点。
- Image Detection V1 支持图片占位文字识别。
- 支持 logo / product image / label image / package image / stamp / signature role 推断。

输入：
- 调用方提供的候选标识、Coordinate、角色和元数据。

输出：
- ImageAreaCandidate。
- ImageAnchorCandidate。

Image Detection V1：
- 识别包含 image、product image、label image、package image、packaging image、logo、stamp、signature 的单元格文本。
- 识别包含 图片、产品图片、标签图片、包装图片、商标、印章、签名 的单元格文本。
- 使用命中单元格的 Coordinate 作为图片占位坐标。
- 不处理真实图片插入。

禁止：
- 不读取真实图片文件。
- 不识别图片内容。
- 不插入图片。
- 不生成 ImageNode。
- 不生成导出操作。
- 不执行图片导出。
- 不扫描嵌入图片对象。
- 不推断图片尺寸。
- 不绑定图片文件。
- 不处理复杂锚点。
