from models.result import Result
from models.segment import Segment
from processors.angles_processor import ANGLE_TYPES
from processors.base import Processor
from utils.config import read_config_file
from utils.constants import COMPARISON_FEATURES_NAME, ConfigFiles
from utils.dtw import (filter_repetable_reference_indexes,
                       get_warped_frame_indexes)


class ResultsProcessor(Processor):
    """
    Processor of differences between query and reference values
    """

    def __init__(self, reference_segement: Segment, exercise: str) -> None:
        super().__init__()
        self.reference_segment = reference_segement
        config_file = read_config_file(ConfigFiles.EXERCISES_TABLES)
        self.comparison_features = config_file[exercise][COMPARISON_FEATURES_NAME]

    def process(self, data: Segment) -> Result:
        query = data
        results = []
        for feature in self.comparison_features:
            for angle_type in ANGLE_TYPES.keys():
                angle_name = feature + "_" + angle_type
                query = [
                    angle.value for angle in data.angles if angle.name == angle_name
                ]
                reference = [
                    angle.value
                    for angle in self.reference_segment.angles
                    if angle.name == angle_name
                ]
                path = get_warped_frame_indexes(query, reference)
                query_to_reference_warping = filter_repetable_reference_indexes(
                    path[:, 1], path[:, 0]
                )
                for reference_idx, query_idx in enumerate(query_to_reference_warping):
                    diff = reference[reference_idx] - query[query_idx]
                    results.append(Result(reference_idx + 1, angle_name, diff))

        return results

    def update(self, data: list[Result]) -> None:
        self.data.append(data)
