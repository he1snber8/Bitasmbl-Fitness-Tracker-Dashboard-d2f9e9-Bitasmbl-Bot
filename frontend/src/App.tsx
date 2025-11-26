import { useEffect, useState } from "react";
import { getJson } from "./api/client";
import { WorkoutForm } from "./components/WorkoutForm";
interface Workout { id: number; type: string; duration_min: number; calories: number; }
const USER_ID = 1;
function App() {
  const [workouts, setWorkouts] = useState<Workout[]>([]);
  async function load() {
    const data = await getJson(`/workouts/user/${USER_ID}`);
    setWorkouts(data as Workout[]);
  }
  useEffect(() => { load(); }, []);
  return (
    <div>
      <h1>Fitness Tracker Dashboard</h1>
      <WorkoutForm userId={USER_ID} onCreated={load} />
      <ul>
        {workouts.map(w => (
          <li key={w.id}>{w.type} - {w.duration_min} min - {w.calories} kcal</li>
        ))}
      </ul>
    </div>
  );
}
export default App;