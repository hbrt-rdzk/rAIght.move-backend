from models.joint import Joint
from pydantic import BaseModel


class ExplainRequest(BaseModel):
    """
    Request for explain
    """

    exercise: str
    fps: int
    joints_data: list[Joint]
