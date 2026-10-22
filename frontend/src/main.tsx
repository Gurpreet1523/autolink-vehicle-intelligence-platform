import React, { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";

const API = import.meta.env.VITE_API_URL || "http://localhost:8000";

type Vehicle = {
  vehicle_id: string;
  model: string;
  software_version: string;
  status: string;
};

type Telemetry = {
  speed: number;
  battery: number;
  motor_temperature: number;
  timestamp: string;
};

function App() {
  const [vehicle, setVehicle] = useState<Vehicle | null>(null);
  const [telemetry, setTelemetry] = useState<Telemetry | null>(null);
  const vehicleId = "VEH-1001";

  useEffect(() => {
    const load = async () => {
      const v = await fetch(`${API}/vehicles/${vehicleId}`).then(r => r.json());
      setVehicle(v);
      const t = await fetch(`${API}/vehicles/${vehicleId}/telemetry?limit=1`).then(r => r.json());
      if (t.length) setTelemetry(t[0]);
    };
    load();
    const timer = setInterval(load, 3000);
    return () => clearInterval(timer);
  }, []);

  return (
    <main style={{fontFamily:"Arial", maxWidth:900, margin:"40px auto"}}>
      <h1>Connected Vehicle Platform</h1>
      <p>Virtual ECU telemetry monitoring</p>

      <section style={{display:"grid", gridTemplateColumns:"repeat(4,1fr)", gap:16}}>
        <Card title="Vehicle" value={vehicle?.vehicle_id || "Loading..."} />
        <Card title="Status" value={vehicle?.status || "Loading..."} />
        <Card title="Battery" value={telemetry ? `${telemetry.battery}%` : "--"} />
        <Card title="Speed" value={telemetry ? `${telemetry.speed} km/h` : "--"} />
      </section>

      <section style={{marginTop:30}}>
        <h2>Vehicle Health</h2>
        <p>Motor temperature: {telemetry ? `${telemetry.motor_temperature} °C` : "--"}</p>
        <p>Software: {vehicle?.software_version || "--"}</p>
        <p>Latest telemetry: {telemetry?.timestamp || "--"}</p>
      </section>
    </main>
  );
}

function Card({title, value}:{title:string,value:string}) {
  return <div style={{border:"1px solid #ddd", padding:20, borderRadius:8}}>
    <small>{title}</small>
    <h2>{value}</h2>
  </div>;
}

createRoot(document.getElementById("root")!).render(<App />);
