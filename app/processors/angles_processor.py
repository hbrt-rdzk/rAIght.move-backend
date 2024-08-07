import numpy as np
import pandas as pd

from app.models.angle import Angle
from app.models.joint import Joint
from app.processors.base import Processor
from app.utils.config import read_config_file
from app.utils.constants import (
    ANGLES_NAME,
    MEDIAPIPE_ANGLE_TYPES,
    ConfigFiles,
    PoseEstimatorModels,
)


class AnglesProcessor(Processor):
    def __init__(self) -> None:
        super().__init__()
        config_file = read_config_file(ConfigFiles.POSE_ESTIMATORS.value)
        self.angle_names = config_file[PoseEstimatorModels.MEDIAPIPE.value][ANGLES_NAME]

    def process(self, data: list[Joint]) -> list[Angle]:
        frames = max(joint.frame for joint in data) + 1
        all_angles = []
        for frame in range(1, frames):
            frame_data = [joint for joint in data if joint.frame == frame]
            joint_dict = {joint.id: [joint.x, joint.y, joint.z] for joint in frame_data}

            for angle_name, joint_ids in self.angle_names.items():
                coords = np.array([joint_dict[joint_id] for joint_id in joint_ids])
                for angle_type, angle_dims in MEDIAPIPE_ANGLE_TYPES.items():
                    angle = self._calculate_angle(*coords, angle_dims)
                    all_angles.append(
                        Angle(
                            frame=frame,
                            name=f"{angle_name}_{angle_type}",
                            value=angle,
                        )
                    )
        return all_angles

    def update(self, data: list[Angle]) -> None:
        self.data.extend(data)

    @staticmethod
    def to_df(data: list[Angle]) -> pd.DataFrame:
        df = pd.DataFrame([angle.model_dump() for angle in data])
        df_reshaped = df.pivot(index="frame", columns="name", values="value")
        return df_reshaped

    @staticmethod
    def from_df(df: pd.DataFrame) -> list[Angle]:
        value_vars = df.columns
        df_melted = df.melt(
            id_vars=["frame"],
            value_vars=value_vars,
            var_name="angle_name",
            value_name="value",
        )
        angles = []
        for _, angle in df_melted.iterrows():
            angles.append(
                Angle(
                    frame=angle["frame"], name=angle["angle_name"], value=angle["value"]
                )
            )
        return angles

    @staticmethod
    def _calculate_angle(
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
