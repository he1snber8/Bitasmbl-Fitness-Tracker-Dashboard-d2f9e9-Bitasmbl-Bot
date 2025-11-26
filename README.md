# Bitasmbl-Fitness-Tracker-Dashboard-d2f9e9-Bitasmbl-Bot

## Description
Build a web and optional mobile dashboard that tracks user workouts, steps, and calories. The project focuses on integrating APIs, storing data in a database, and displaying interactive charts and statistics.

## Tech Stack
- FastAPI
- React
- Flutter (optional/mobile)
- PostgreSQL

## Requirements
- Track user workouts, steps, and calorie intake
- Display data visually in charts or graphs
- Allow users to input new workout sessions
- Store user data persistently in a database
- Optionally support mobile-friendly access or apps

## Installation
bash
git clone https://github.com/he1snber8/Bitasmbl-Fitness-Tracker-Dashboard-d2f9e9-Bitasmbl-Bot.git
cd Bitasmbl-Fitness-Tracker-Dashboard-d2f9e9-Bitasmbl-Bot
# Backend
cd backend
pip install fastapi uvicorn psycopg2-binary
# Frontend
cd ../frontend
npm install
# Mobile (optional)
cd ../mobile
flutter pub get


## Usage
bash
# Backend
cd backend
uvicorn main:app --reload
# Frontend
cd ../frontend
npm start
# Mobile (optional)
cd ../mobile
flutter run


## Implementation Steps
1. Define PostgreSQL schema for users, workouts, steps, and calories.
2. Implement FastAPI models and CRUD operations for tracking data.
3. Expose API endpoints for workouts, steps, and calorie intake.
4. Connect FastAPI to PostgreSQL for persistent storage.
5. Build React dashboard to display charts and statistics using API data.
6. Add forms in React to input new workout sessions.
7. Implement optional Flutter app consuming the same FastAPI APIs.
8. Ensure responsive layout for mobile-friendly web access.

## API Endpoints
- POST /workouts
- GET /workouts
- POST /steps
- GET /steps
- POST /calories
- GET /calories