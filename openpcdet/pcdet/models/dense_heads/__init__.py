from .anchor_head_multi import AnchorHeadMulti
from .anchor_head_single import AnchorHeadSingle
from .anchor_head_template import AnchorHeadTemplate
from .center_head_single import CenterHead
from .point_head_box import PointHeadBox
from .point_head_simple import PointHeadSimple
from .point_intra_part_head import PointIntraPartOffsetHead

__all__ = {
    "AnchorHeadTemplate": AnchorHeadTemplate,
    "AnchorHeadSingle": AnchorHeadSingle,
    "PointIntraPartOffsetHead": PointIntraPartOffsetHead,
    "PointHeadSimple": PointHeadSimple,
    "PointHeadBox": PointHeadBox,
    "AnchorHeadMulti": AnchorHeadMulti,
    "CenterHead": CenterHead,
}
