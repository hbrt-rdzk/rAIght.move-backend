from pydantic import BaseModel


class Mistake(BaseModel):
    """
    Mistake object that handles feedback
    """

    exercise: str
    mistake_name: str
    fix_info: str
    angle_name: str
    threshold: float
