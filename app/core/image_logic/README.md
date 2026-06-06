目录：
app/core/image_logic

职责：
提供图片逻辑（Image Logic）的基础结构化能力。

当前能力：
- 定义图片区域候选（ImageAreaCandidate）。
- 定义图片锚点候选（ImageAnchorCandidate）。
- 使用 Coordinate 表达候选区域和锚点。

输入：
- 调用方提供的候选标识、Coordinate、角色和元数据。

输出：
- ImageAreaCandidate。
- ImageAnchorCandidate。

禁止：
- 不读取真实图片文件。
- 不识别图片内容。
- 不插入图片。
- 不生成 ImageNode。
- 不生成导出操作。
- 不执行图片导出。
