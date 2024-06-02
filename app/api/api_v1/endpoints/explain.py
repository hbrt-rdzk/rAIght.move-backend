from core.exercise_explaination_pipeline import Pipeline
from fastapi import APIRouter
from models.joint import Joint
from models.mistake import Mistake

router = APIRouter()


@router.get("/", response_model=Mistake)
def explain() -> Mistake:
    return Pipeline().run()
