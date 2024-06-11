import pandas as pd

from app.models.result import Result
from app.models.segment import Segment
from app.processors.angles_processor import ANGLE_TYPES, AnglesProcessor
from app.processors.base import Processor
from app.utils.config import read_config_file
from app.utils.constants import (COMPARISON_FEATURES_NAME,
                                 REFERENCE_SEGMENT_PATH, ConfigFiles)
from app.utils.dtw import (filter_repetable_reference_indexes,
                           get_warped_frame_indexes)


class ResultsProcessor(Processor):
    """
    Processor of differences between query and reference values
    """

    def __init__(self, exercise: str) -> None:
        super().__init__()
        reference_segment_path = REFERENCE_SEGMENT_PATH.format(exercise=exercise)
        self.reference_segment = self.load_segment(reference_segment_path)

        config_file = read_config_file(ConfigFiles.EXERCISES_TABLES.value)
        self.comparison_features = config_file[exercise][COMPARISON_FEATURES_NAME]

    def process(self, data: list[Segment]) -> list[Result]:
        results = []
        for segment in data:
            for feature in self.comparison_features:
                for angle_type in ANGLE_TYPES.keys():
                    angle_name = feature + "_" + angle_type
                    query = [
                        angle.value
                        for angle in segment.angles
                        if angle.name == angle_name
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
                    for reference_idx, query_idx in enumerate(
                        query_to_reference_warping
                    ):
                        diff = reference[reference_idx] - query[query_idx]
                        results.append(
                            Result(
                                frame=segment.start_frame + query_idx,
                                repetition=segment.repetition,
                                angle_name=angle_name,
                                diff=diff,
                            )
                        )
        return results

    def update(self, data: list[Result]) -> None:
        self.data.append(data)

    @staticmethod
    def load_segment(data_path: str) -> Segment:
        df = pd.read_csv(data_path)
        angles = AnglesProcessor.from_df(df)
        return Segment(
            repetition=0,
            start_frame=angles[0].frame,
            finish_frame=angles[-1].frame,
            angles=angles,
        )
