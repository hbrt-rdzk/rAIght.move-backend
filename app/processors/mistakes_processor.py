from app.models.mistake import Mistake
from app.models.result import Result
from app.processors.base import Processor
from app.utils.config import read_config_file
from app.utils.constants import (ANGLE_NAME_KEY, ERRORS_KEY, FIX_INFO_KEY,
                                 MISTAKES_TABLE_NAME, THRESHOLD_KEY,
                                 ConfigFiles)


class MistakesProcessor(Processor):
    def __init__(self, exercise: str) -> None:
        super().__init__()
        config_file = read_config_file(ConfigFiles.EXERCISES_TABLES.value)
        mistakes_table = config_file[exercise][MISTAKES_TABLE_NAME]
        self.mistake_templates = self._get_mistake_templates(mistakes_table, exercise)

    def process(self, data: list[Result]) -> list[Mistake]:
        # TODO: improve this
        mistakes = []
        segments = max(result.repetition for result in data) + 1
        for segment in range(1, segments):
            segment_data = [result for result in data if result.repetition == segment]
            for mistake_template in self.mistake_templates:
                for result in segment_data:
                    if (result.angle_name == mistake_template.angle_name) and (
                        abs(result.diff) > mistake_template.threshold
                    ):
                        mistake_template.repetition = segment
                        mistakes.append(mistake_template)
                        break
        return mistakes

    def update(self, data: list[Mistake]) -> None:
        self.data = data

    @staticmethod
    def _get_mistake_templates(mistakes_table: dict, exercise: str) -> list[Mistake]:
        mistake_templates = []
        for mistake_name, mistake_data in mistakes_table.items():
            fix_info = mistake_data[FIX_INFO_KEY]
            for error in mistake_data[ERRORS_KEY]:
                mistake_templates.append(
                    Mistake(
                        exercise=exercise,
                        repetition=0,
                        mistake_name=mistake_name,
                        fix_info=fix_info,
                        angle_name=error[ANGLE_NAME_KEY],
                        threshold=error[THRESHOLD_KEY],
                    )
                )
        return mistake_templates
