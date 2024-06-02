from pydantic import BaseModel


class Joint(BaseModel):
    """
    Joint extracted by DNN model from video
    """

    frame: int
    id: int
    name: str
    x: float
    y: float
    z: float
    visibility: float
