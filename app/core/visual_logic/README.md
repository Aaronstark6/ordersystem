目录：
app/core/visual_logic

职责：
视觉逻辑（Visual Logic）。

当前能力：
- Coordinate。
- CoordinateGroup。
- VisualRegionCandidate。
- LayoutRegionCandidate。
- AnchorCandidate。

当前原则：
- Coordinate 是唯一坐标标准。
- 所有视觉区域、布局区域、锚点和坐标组都复用 Coordinate。

当前 Coordinate（坐标）支持：
- Excel 单元格坐标（Excel Cell Coordinate）。
- PDF 绝对坐标（PDF Absolute Coordinate）。
- Word 结构坐标（Word Structural Coordinate）。

Word 结构坐标字段：
- paragraph_index。
- table_index。
- bookmark。
- placeholder。

禁止：
- 第二套坐标体系。
- CoordinateV2。
- PdfCoordinate。
- WordCoordinate。
- VisualCoordinate。
- AnchorCoordinate。
- CellCoordinate。
- TargetCoordinate。
- SourceCoordinate。
