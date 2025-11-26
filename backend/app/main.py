from fastapi import FastAPI
from .routers import workouts
from .database import init_db
app = FastAPI(title="Fitness Tracker API")
@app.on_event("startup")
async def startup():
    await init_db()
app.include_router(workouts.router, prefix="/workouts", tags=["workouts"])
@app.get("/health")
async def health():
    return {"status": "ok"}