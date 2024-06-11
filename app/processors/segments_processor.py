from collections import defaultdict

import numpy as np
from scipy.signal import find_peaks

from app.models.angle import Angle
from app.models.segment import Segment
from app.processors.base import Processor
from app.utils.config import read_config_file
from app.utils.constants import SEGMENTATION_FEATURES_NAME, ConfigFiles


class SegmentsProcessor(Processor):
    def __init__(self, exercise: str, fps: int) -> None:
        super().__init__()
        self.fps = fps
        config_file = read_config_file(ConfigFiles.EXERCISES_TABLES.value)
        self.segmentaion_features = config_file[exercise][SEGMENTATION_FEATURES_NAME]

    def process(self, data: list[Angle]) -> list[Segment]:
        angles = data
        peaks, valleys = self._get_peaks_and_valleys(angles)
        segments_frames = self._get_segments_indexes(peaks, valleys)

        segments = []
        for rep, (start_frame, finish_frame) in enumerate(segments_frames, 1):
            segment_angles = [
                angle for angle in angles if start_frame <= angle.frame <= finish_frame
            ]
            segments.append(
                Segment(
                    repetition=rep,
                    angles=segment_angles,
                    start_frame=start_frame,
                    finish_frame=finish_frame,
                )
            )
        return segments

    def update(self, data: list[Segment]) -> None:
        self.data = data

    def _get_peaks_and_valleys(self, angles: list[Angle]) -> np.ndarray:
        data = defaultdict(list)
        for angle in angles:
            if angle.name in self.segmentaion_features:
                data[angle.frame].append(angle.value)

        exercise_signal = np.array([np.mean(values) for values in data.values()])
        zero_point = np.mean(exercise_signal)

        peaks, _ = find_peaks(exercise_signal, zero_point)
        valleys, _ = find_peaks(-exercise_signal, -zero_point)
        return peaks, valleys

    def _get_segments_indexes(
        self, peaks: np.ndarray, valleys: np.ndarray
    ) -> list[list[int, int]]:
        segments = []
        valley_idx = 0
        peaks_idx = 0
        while peaks_idx < len(peaks) - 1:
            if peaks[peaks_idx] < valleys[valley_idx]:
                if peaks[peaks_idx + 1] < valleys[valley_idx]:
                    peaks[peaks_idx + 1] = (
                        peaks[peaks_idx] + peaks[peaks_idx + 1]
                    ) // 2
                else:
                    segments.append([peaks[peaks_idx], peaks[peaks_idx + 1]])
                peaks_idx += 1

            else:
                if valley_idx >= len(valleys) - 1:
                    break
                if valleys[valley_idx + 1] < peaks[peaks_idx]:
                    valleys[valley_idx + 1] = (
                        valleys[valley_idx] + valleys[valley_idx + 1]
                    ) // 2
                valley_idx += 1
        return segments
