from enum import Enum


class ConfigFiles(Enum):
    POSE_ESTIMATORS = "configs/pose_estimators.yaml"
    EXERCISES_TABLES = "configs/exercises_tables.yaml"


class PoseEstimatorModels(Enum):
    OPENPOSE = "openpose"
    MEDIAPIPE = "mediapipe"


JOINTS_NAME = "joints"
ANGLES_NAME = "angles"

SEGMENTATION_FEATURES_NAME = "segment_angles"
COMPARISON_FEATURES_NAME = "comparison_features"
MISTAKES_TABLE_NAME = "mistakes_table"

MEDIAPIPE_ANGLE_TYPES = {
    "3D": [0, 1, 2],
    "top": [0, 2],
    "side": [0, 1],
    "front": [1, 2],
}

REFERENCE_SEGMENT_PATH = "data/reference/{exercise}/segment.csv"

FIX_INFO_KEY = "fix_info"
ANGLE_NAME_KEY = "angle_name"
THRESHOLD_KEY = "threshold"
ERRORS_KEY = "errors"
