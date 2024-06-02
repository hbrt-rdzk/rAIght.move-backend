from pydantic import BaseModel

ANGLE_PARAMETERS_NUM = 3
ANGLES_PER_FRAME = 8


class Angle(BaseModel):
    """
    Angle calculated from joint positions
    """

    frame: int
    name: str
    value: float
