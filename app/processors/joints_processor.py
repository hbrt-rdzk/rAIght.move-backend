from typing import Any

from models.joint import Joint
from processors.base import Processor
from utils.config import read_config_file
from utils.constants import JOINTS_NAME, ConfigFiles, PoseEstimatorModels


class JointsProcessor(Processor):
    """
    Procssor of the joints in 3D space
    """

    current_processing_frame = 1

    def __init__(self) -> None:
        super().__init__()
        config_file = read_config_file(ConfigFiles.POSE_ESTIMATORS.value)
        self.joint_names = config_file[PoseEstimatorModels.MEDIAPIPE.value][JOINTS_NAME]

    def process(self, data: Any) -> list[Joint]:
        return [
            Joint(
                frame=self.current_processing_frame,
                id=idx,
                name=self.joint_names[idx],
                x=joint.x,
                y=joint.y,
                z=joint.z,
                visibility=joint.visibility,
            )
            for idx, joint in enumerate(data.landmark)
            if idx in self.joint_names.keys()
        ]

    def update(self, data: list[Joint]) -> None:
        self.data.extend(data)
