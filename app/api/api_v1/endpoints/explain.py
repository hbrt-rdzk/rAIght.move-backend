from core.processing_pipeline import Pipeline
from fastapi import APIRouter
from models.joint import Joint
from models.mistake import Mistake
from processors.angles_processor import AnglesProcessor
from processors.mistakes_processor import MistakesProcessor
from processors.results_processor import ResultsProcessor
from processors.segments_processor import SegmentsProcessor

router = APIRouter()


@router.get("/", response_model=list[Mistake])
def explain(exercise: str, joints_data: list[Joint]) -> list[Mistake]:
    angle_processor = AnglesProcessor()
    segments_processor = SegmentsProcessor()
    results_processor = ResultsProcessor(exercise)
    mistakes_procesor = MistakesProcessor(exercise)
    pipeline = Pipeline(
        [angle_processor, segments_processor, results_processor, mistakes_procesor]
    )
    return pipeline.run(joints_data)
