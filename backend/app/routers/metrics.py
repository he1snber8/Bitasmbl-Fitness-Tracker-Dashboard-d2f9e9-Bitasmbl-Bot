from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import SessionLocal
router = APIRouter()
async def get_db():
    async with SessionLocal() as session:
        yield session
@router.get("/summary/{user_id}")
async def get_summary(user_id: int, db: AsyncSession = Depends(get_db)):
    # TODO: aggregate steps and calories over recent days
    return {"user_id": user_id, "days": []}