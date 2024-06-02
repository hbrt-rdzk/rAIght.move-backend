from models.angle import Angle
from models.joint import Joint
from pydantic import BaseModel


class Segment(BaseModel):
    """
    One exercise repetition features
    """

    start_frame: int
    finish_frame: int
    rep: int
    joints: list[Joint]
    angles: list[Angle]
