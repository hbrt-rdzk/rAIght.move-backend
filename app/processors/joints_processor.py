from typing import Any

from app.models.joint import Joint, RequestJoint
from app.processors.base import Processor
from app.utils.config import read_config_file
from app.utils.constants import JOINTS_NAME, ConfigFiles, PoseEstimatorModels


class JointsProcessor(Processor):
    """
    Procssor of the joints in 3D space
    """

    def __init__(self) -> None:
        super().__init__()
        config_file = read_config_file(ConfigFiles.POSE_ESTIMATORS.value)
        self.joint_names = config_file[PoseEstimatorModels.MEDIAPIPE.value][JOINTS_NAME]

    def process(self, data: list[RequestJoint]) -> list[Joint]:
        return [
            Joint(
                frame=joint.frame,
                id=joint.id,
                name=self.joint_names[joint.id],
                x=joint.x,
                y=joint.y,
                z=joint.z,
                visibility=joint.visibility,
            )
            for joint in data
            if joint.id in self.joint_names.keys()
        ]

    def update(self, data: list[Joint]) -> None:
        self.data.extend(data)
