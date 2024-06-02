from pydantic import BaseModel


class Result(BaseModel):
    """
    Results from frame comparison
    """

    frame: int
    angle_name: str
    diff: float
