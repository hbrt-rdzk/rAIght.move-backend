from models.angle import Angle
from models.joint import Joint
from pydantic import BaseModel


class Segment(BaseModel):
    """
    One exercise repetition features
    """

    repetition: int
    angles: list[Angle]
    start_frame: int
    finish_frame: int
