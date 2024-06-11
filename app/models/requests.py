from pydantic import BaseModel

from app.models.joint import Joint


class ExplainRequest(BaseModel):
    """
    Request for explain
    """

    exercise: str
    fps: int
    joints_data: list[Joint]
