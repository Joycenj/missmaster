import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import Nav from "@/components/Nav";
import { getCandidate, createVoteIntent, getVoteIntent } from "@/components/Api";

export default function CandidateDetail(){
  const router = useRouter();
  const { slug } = router.query;
  const [c, setC] = useState(null);
  const [votes, setVotes] = useState(1);
  const [phone, setPhone] = useState("");
  const [provider, setProvider] = useState("MTN");
  const [intent, setIntent] = useState(null);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);

  useEffect(()=>{
    if(!slug) return;
    (async ()=>{
      try{
        const data = await getCandidate(slug);
        setC(data);
      } finally {
        setLoading(false);
      }
    })();
  },[slug]);

  async function pay(){
    if(!c) return;
    if(!phone){ alert("Enter phone number (6XXXXXXXX)"); return; }
    if(votes < 1){ alert("Votes must be at least 1"); return; }
    setSubmitting(true);
    try{
      const res = await createVoteIntent({
        candidate_id: c.id, votes_requested: votes, payer_phone: phone, provider
      });
      setIntent(res);
      // Polling
      const interval = setInterval(async ()=>{
        const st = await getVoteIntent(res.intent_id);
        if(st.status === "PAID"){ clearInterval(interval); router.push("/success"); }
        if(st.status === "FAILED"){ clearInterval(interval); alert("Payment failed"); }
      }, 5000);
    } catch (e){
      alert("Failed to create payment. Check backend is running.");
    } finally {
      setSubmitting(false);
    }
  }

  if(loading) return <div><Nav/><main className="container py-8">Loading…</main></div>;
  if(!c) return <div><Nav/><main className="container py-8">Candidate not found.</main></div>;

  return (
    <>
      <Nav/>
      <main className="container py-8">
        <div className="grid md:grid-cols-2 gap-6">
          <img src={c.photo_src} alt={c.display_name} className="w-full h-96 object-cover rounded-xl"/>
          <div>
            <h1 className="text-3xl font-bold">{c.display_name}</h1>
            {c.short_description && <p className="text-gray-600 mt-2">{c.short_description}</p>}
            {c.bio && <p className="text-gray-600 mt-2">{c.bio}</p>}
            <div className="text-sm text-gray-500 mt-2">Votes: {c.votes_count}</div>

            <div className="mt-6 p-4 border rounded-xl space-y-3">
              <div>
                <label className="label">Votes</label>
                <input type="number" min={1} value={votes} onChange={e=>setVotes(parseInt(e.target.value || "1"))} className="input w-32"/>
              </div>
              <div>
                <label className="label">Phone</label>
                <input value={phone} onChange={e=>setPhone(e.target.value)} placeholder="6XXXXXXXX" className="input"/>
              </div>
              <div>
                <label className="label">Provider</label>
                <select value={provider} onChange={e=>setProvider(e.target.value)} className="select">
                  <option value="MTN">MTN MoMo</option>
                  <option value="ORANGE">Orange Money</option>
                </select>
              </div>
              <button onClick={pay} disabled={submitting} className="btn btn-primary">{submitting ? "Processing…" : "Pay & Vote"}</button>
              {intent && <p className="text-sm text-gray-500">Waiting for payment… Ref: {intent.payment_ref}</p>}
            </div>
          </div>
        </div>
      </main>
    </>
  )
}
