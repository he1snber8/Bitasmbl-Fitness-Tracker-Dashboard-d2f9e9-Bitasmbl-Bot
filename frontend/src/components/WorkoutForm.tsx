import { useState, FormEvent } from "react";
import { postJson } from "../api/client";
export function WorkoutForm({ userId, onCreated }: { userId: number; onCreated: () => void }) {
  const [type, setType] = useState("");
  const [duration, setDuration] = useState(30);
  const [calories, setCalories] = useState(200);
  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    await postJson("/workouts/", {
      user_id: userId,
      type,
      duration_min: duration,
      calories,
      timestamp: new Date().toISOString(),
    });
    onCreated();
  }
  return (
    <form onSubmit={handleSubmit}>
      <input value={type} onChange={e => setType(e.target.value)} placeholder="Workout type" />
      <input type="number" value={duration} onChange={e => setDuration(+e.target.value)} />
      <input type="number" value={calories} onChange={e => setCalories(+e.target.value)} />
      <button type="submit">Add Workout</button>
    </form>
  );
}