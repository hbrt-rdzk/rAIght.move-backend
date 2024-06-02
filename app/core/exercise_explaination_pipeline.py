from models.joint import Joint
from models.mistake import Mistake


class Pipeline:
    def __init__(self) -> None:
        pass

    @staticmethod
    def run() -> list[Mistake]:
        return Mistake(
            exercise="squat",
            mistake_name="squat",
            fix_info="squat",
            angle_name="squat",
            threshold=0.5,
        )
