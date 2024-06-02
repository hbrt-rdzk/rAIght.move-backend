from pydantic import BaseModel


class Angle(BaseModel):
    """
    Angle calculated from joint positions
    """

    frame: int
    name: str
    value: float
