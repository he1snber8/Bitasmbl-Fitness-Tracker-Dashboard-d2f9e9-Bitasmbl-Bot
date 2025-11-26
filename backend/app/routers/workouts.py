from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import SessionLocal
from .. import models, schemas
router = APIRouter()
async def get_db():
    async with SessionLocal() as session:
        yield session
@router.post("/", response_model=schemas.WorkoutRead)
async def create_workout(payload: schemas.WorkoutCreate, db: AsyncSession = Depends(get_db)):
    obj = models.WorkoutSession(**payload.dict())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj
@router.get("/user/{user_id}")
async def list_workouts(user_id: int, db: AsyncSession = Depends(get_db)):
    q = await db.execute(models.WorkoutSession.__table__.select().where(models.WorkoutSession.user_id==user_id))
    return q.fetchall()