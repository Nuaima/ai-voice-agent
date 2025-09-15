import { useState } from 'react';

export default function CallForm({ onCallTriggered }) {
  const [driverName, setDriverName] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [loadNumber, setLoadNumber] = useState('');

  const startCall = async () => {
    const res = await fetch("http://localhost:8000/start-call", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ driver_name: driverName, phone_number: phoneNumber, load_number: loadNumber })
    });
    const data = await res.json();
    alert(data.message);
    if (onCallTriggered) onCallTriggered();
  };

  return (
    <div>
      <input placeholder="Driver Name" value={driverName} onChange={e => setDriverName(e.target.value)} />
      <input placeholder="Phone Number" value={phoneNumber} onChange={e => setPhoneNumber(e.target.value)} />
      <input placeholder="Load Number" value={loadNumber} onChange={e => setLoadNumber(e.target.value)} />
      <button onClick={startCall}>Start Call</button>
    </div>
  );
}
