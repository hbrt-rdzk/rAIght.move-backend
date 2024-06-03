from core.processing_pipeline import Pipeline
from fastapi import APIRouter
from models.mistake import Mistake
from models.requests import ExplainRequest
from processors.angles_processor import AnglesProcessor
from processors.mistakes_processor import MistakesProcessor
from processors.results_processor import ResultsProcessor
from processors.segments_processor import SegmentsProcessor

router = APIRouter()


@router.post("/", response_model=list[Mistake])
def explain(request: ExplainRequest) -> list[Mistake]:
    angle_processor = AnglesProcessor()
    segments_processor = SegmentsProcessor(request.fps)
    results_processor = ResultsProcessor(request.exercise)
    mistakes_procesor = MistakesProcessor(request.exercise)
    pipeline = Pipeline(
        [angle_processor, segments_processor, results_processor, mistakes_procesor]
    )
    return pipeline.run(request.joints_data)
