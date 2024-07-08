from pydantic import BaseModel


class RequestJoint(BaseModel):
    """
    Joint extracted by DNN model from video
    """

    frame: int
    id: int
    x: float
    y: float
    z: float
    visibility: float


class Joint(RequestJoint):
    name: str
