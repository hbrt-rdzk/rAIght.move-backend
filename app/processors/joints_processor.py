from typing import Any

from models.joint import JOINT_PARAMETERS_NUM, Joint
from processors.base import Processor


class JointsProcessor(Processor):
    """
    Procssor of the joints in 3D space
    """

    current_processing_frame = 1

    def __init__(self, joint_names: dict) -> None:
        super().__init__()
        self.joint_names = joint_names

    def __len__(self) -> int:
        return len(self.data) * JOINT_PARAMETERS_NUM

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
