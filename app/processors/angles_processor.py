import numpy as np
from models.angle import ANGLE_PARAMETERS_NUM, Angle
from models.joint import Joint
from processors.base import Processor

# For mediapipe Y is switched with Z
ANGLE_TYPES = {"3D": [0, 1, 2], "roll": [1, 2], "pitch": [0, 1], "yaw": [0, 2]}


class AnglesProcessor(Processor):
    def __init__(self, angle_names: dict) -> None:
        super().__init__()
        self.angle_names = angle_names

    def __len__(self) -> int:
        return len(self.data) * ANGLE_PARAMETERS_NUM

    def process(self, data: list[Joint]) -> list[Angle]:
        frame_number = data[0].frame
        joint_dict = {joint.id: [joint.x, joint.y, joint.z] for joint in data}

        angles = []
        for angle_name, joint_ids in self.angle_names.items():
            coords = np.array([joint_dict[joint_id] for joint_id in joint_ids])
            for angle_type, angle_dims in ANGLE_TYPES.items():
                angle = self.__calculate_angle(*coords, angle_dims)
                angles.append(Angle(frame_number, f"{angle_name}_{angle_type}", angle))

        return angles

    def update(self, data: list[Angle]) -> None:
        self.data.extend(data)

    @staticmethod
    def __calculate_angle(
        v1: np.ndarray, v2: np.ndarray, v3: np.ndarray, dims: list
    ) -> float:
        if not all(arr.shape == (3,) for arr in (v1, v2, v3)):
            raise ValueError("Input arrays must all be of shape (3,).")
        v1 = v1[dims]
        v2 = v2[dims]
        v3 = v3[dims]

        v21 = v1 - v2
        v23 = v3 - v2

        cosine_angle = np.dot(v21, v23) / (np.linalg.norm(v21) * np.linalg.norm(v23))
        angle = np.arccos(cosine_angle)

        return np.degrees(angle)
