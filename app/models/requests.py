from pydantic import BaseModel

from app.models.joint import RequestJoint


class ExplainRequest(BaseModel):
    """
    Request for explain
    """

    exercise: str
    joints_data: list[RequestJoint]
