from typing import Optional, Sequence, Tuple, TypedDict, List, TypeVar
from pathlib import Path
from torch import Tensor
from tokenizers import Encoding


T = TypeVar('T')

KEYPOINT_FORMAT = TypeVar('KEYPOINT_FORMAT')

class ClipData(TypedDict):
    label: str
    start: float
    end: float
    video: float

class KeypointData(TypedDict):
    image_id: str
    category_id: int
    keypoints: List[float]
    score: float
    box: List[float]
    idx: List[float]

class Box(TypedDict):
    x1: float
    y1: float
    width: float
    height: float

class SignerData(TypedDict):
    scores: List[float]
    roi: Box
    keypoints: List[KeypointData]

ClipSample = Tuple[
    dict[str, Path],
    Optional[Tensor],
    Optional[Sequence[KEYPOINT_FORMAT]],
    Encoding]
    # Encoding docs: https://huggingface.co/docs/tokenizers/python/latest/api/reference.html#tokenizers.Encoding
