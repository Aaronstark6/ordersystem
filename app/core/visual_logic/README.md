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

禁止：
- 第二套坐标体系。
- VisualCoordinate。
- AnchorCoordinate。
- CellCoordinate。
- TargetCoordinate。
- SourceCoordinate。
