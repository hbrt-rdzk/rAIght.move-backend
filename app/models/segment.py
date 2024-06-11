from pydantic import BaseModel

from app.models.angle import Angle


class Segment(BaseModel):
    """
    One exercise repetition features
    """

    repetition: int
    angles: list[Angle]
    start_frame: int
    finish_frame: int
