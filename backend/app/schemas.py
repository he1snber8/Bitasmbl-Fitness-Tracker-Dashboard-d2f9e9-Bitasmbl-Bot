from pydantic import BaseModel
from datetime import datetime, date
class WorkoutCreate(BaseModel):
    user_id: int
    type: str
    duration_min: int
    calories: float
    timestamp: datetime
class WorkoutRead(WorkoutCreate):
    id: int
    class Config:
        orm_mode = True
class DailyMetricsRead(BaseModel):
    date: date
    steps: int
    calories_intake: float