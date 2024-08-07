from fastapi import APIRouter

from app.core.processing_pipeline import Pipeline
from app.models.mistake import Mistake
from app.models.requests import ExplainRequest
from app.processors.angles_processor import AnglesProcessor
from app.processors.joints_processor import JointsProcessor
from app.processors.mistakes_processor import MistakesProcessor
from app.processors.results_processor import ResultsProcessor
from app.processors.segments_processor import SegmentsProcessor

router = APIRouter()


@router.post("/", response_model=list[Mistake])
def explain(request: ExplainRequest) -> list[Mistake]:
    joints_processor = JointsProcessor()
    angle_processor = AnglesProcessor()
    segments_processor = SegmentsProcessor(request.exercise)
    results_processor = ResultsProcessor(request.exercise)
    mistakes_procesor = MistakesProcessor(request.exercise)
    pipeline = Pipeline(
        [
            joints_processor,
            angle_processor,
            segments_processor,
            results_processor,
            mistakes_procesor,
        ]
    )
    output = pipeline.run(request.joints_data)
    return output
