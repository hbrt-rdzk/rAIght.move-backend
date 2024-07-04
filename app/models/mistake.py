from pydantic import BaseModel


class Mistake(BaseModel):
    """
    Mistake object that handles feedback
    """

    exercise: str
    repetition: int
    repetition_start_frame: int
    repetition_finish_frame: int
    mistake_name: str
    fix_info: str
    angle_name: str
    threshold: float
