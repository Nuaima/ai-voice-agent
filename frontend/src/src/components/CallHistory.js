import { useEffect, useState } from 'react';
import { supabase } from '../supabaseClient';

export default function CallHistory() {
  const [calls, setCalls] = useState([]);

  useEffect(() => {
    const fetchCalls = async () => {
      const { data, error } = await supabase
        .from("calls")
        .select("*")
        .order("created_at", { ascending: false });
      if (!error) setCalls(data);
    };
    fetchCalls();
  }, []);

  return (
    <div>
      <h2>Call History</h2>
      {calls.map(call => (
        <div key={call.id}>
          <p><b>Driver:</b> {call.driver_name}</p>
          <p><b>Load:</b> {call.load_number}</p>
          <p><b>Transcript:</b> {call.transcript}</p>
          <p><b>Summary:</b> {JSON.stringify(call.summary)}</p>
          <hr />
        </div>
      ))}
    </div>
  );
}
