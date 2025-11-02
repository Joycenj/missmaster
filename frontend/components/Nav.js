export default function Nav(){
  return (
    <>
      {/* Announcement ribbon with crisp gold rule */}
      <div
        className="w-full text-center text-xs sm:text-sm py-1.5 select-none"
        style={{
          background: 'linear-gradient(90deg, rgba(229,195,90,.12), rgba(156,107,48,.12))',
          borderBottom: '1px solid rgba(229,195,90,.55)'
        }}
      >
        <span className="tracking-wide">
          <strong>Miss/Master Nkul-Beti — 17<sup>e</sup> édition</strong> · organisée par l’<strong>Université des Montagne</strong>
        </span>
      </div>

      {/* Main navbar (clean white) */}
      <header className="sticky top-0 z-40 bg-white/85 backdrop-blur border-b"
              style={{ borderColor:'rgba(229,195,90,.45)' }}>
        <div className="container py-3 flex items-center gap-4">
          <a href="/" className="text-xl font-extrabold tracking-wide">
            MissMaster<span style={{color:'#9C6B30'}}>Vote</span>
          </a>
          <nav className="ml-auto flex gap-5 text-sm">
            <a href="/candidates" className="hover:underline decoration-[rgba(229,195,90,.8)] underline-offset-4">Candidats</a>
          </nav>
        </div>
      </header>
    </>
  );
}
