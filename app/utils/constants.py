from enum import Enum


class ConfigFiles(Enum):
    POSE_ESTIMATORS = "config/pose_estimators.yaml"
    EXERCISES_TABLES = "config/exercises_tables.yaml"
    SEGMENTATION = "config/segmentation.yaml"


class PoseEstimatorModels(Enum):
    OPENPOSE = "openpose"
    MEDIAPIPE = "mediapipe"


JOINTS_NAME = "joints"
ANGLES_NAME = "angles"
COMPARISON_FEATURES_NAME = "comparison_features"
SEGMENTATION_PARAMETERS_NAME = "segmentation_parameters"
MISTAKES_TABLE_NAME = "mistakes_table"

ANGLE_TYPES = {"3D": [0, 1, 2], "roll": [1, 2], "pitch": [0, 1], "yaw": [0, 2]}


FIX_INFO_KEY = "fix_info"
ANGLE_NAME_KEY = "angle_name"
THRESHOLD_KEY = "threshold"
ERRORS_KEY = "errors"
