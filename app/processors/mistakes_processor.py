from models.mistake import Mistake
from models.result import Result
from processors.base import Processor
from utils.config import read_config_file
from utils.constants import MISTAKES_TABLE_NAME, ConfigFiles


class MistakesProcessor(Processor):
    def __init__(self, exercise: str) -> None:
        super().__init__()
        config_file = read_config_file(ConfigFiles.EXERCISES_TABLES)
        mistakes_table = config_file[exercise][MISTAKES_TABLE_NAME]
        self.mistake_templates = self.__get_mistake_templates(mistakes_table, exercise)

    def process(self, data: list[Result]) -> list[Mistake]:
        # TODO: improve this
        mistakes = [
            mistake_template
            for mistake_template in self.mistake_templates
            for result in data
            if result.angle_name == mistake_template.angle_name
            and abs(result.diff) > mistake_template.threshold
        ]
        return list(set(mistakes))

    def update(self, data: list[Mistake]) -> None:
        self.data.append(data)

    @staticmethod
    def __get_mistake_templates(mistakes_table: dict, exercise: str) -> list[Mistake]:
        mistake_templates = []
        for mistake_name, mistake_data in mistakes_table.items():
            fix_info = mistake_data[FIX_INFO_KEY]
            for error in mistake_data[ERRORS_KEY]:
                mistake_templates.append(
                    Mistake(
                        exercise=exercise,
                        mistake_name=mistake_name,
                        fix_info=fix_info,
                        angle_name=error[ANGLE_NAME_KEY],
                        threshold=error[THRESHOLD_KEY],
                    )
                )
        return mistake_templates
