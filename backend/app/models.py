from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Date
Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
class WorkoutSession(Base):
    __tablename__ = "workouts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String)
    duration_min = Column(Integer)
    calories = Column(Float)
    timestamp = Column(DateTime)
class DailyMetrics(Base):
    __tablename__ = "daily_metrics"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date)
    steps = Column(Integer)
    calories_intake = Column(Float)