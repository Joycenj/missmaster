import Nav from "../components/Nav";


function CrownIcon(props){
  return (
    <svg viewBox="0 0 64 24" width="64" height="24" aria-hidden="true" {...props}>
      <path d="M6 18L14 6l6 8 12-12 6 12 8-8 6 12H6z" fill="url(#g)" />
      <circle cx="14" cy="6" r="2" fill="#FFD700" opacity="0.8"/>
      <circle cx="20" cy="14" r="1.5" fill="#FFD700" opacity="0.8"/>
      <circle cx="32" cy="2" r="2.5" fill="#FFD700" opacity="0.9"/>
      <circle cx="38" cy="14" r="1.5" fill="#FFD700" opacity="0.8"/>
      <circle cx="46" cy="6" r="2" fill="#FFD700" opacity="0.8"/>
      <defs>
        <linearGradient id="g" x1="0" y1="0" x2="64" y2="24" gradientUnits="userSpaceOnUse">
          <stop offset="0" stopColor="#D4AF37"/>
          <stop offset="0.5" stopColor="#F4E4C1"/>
          <stop offset="1" stopColor="#8B6914"/>
        </linearGradient>
      </defs>
    </svg>
  );
}

export default function Home(){
  return (
    <>
      <Nav/>
      <div className="landing-bg">
        <main className="container py-20 sm:py-24 landing-content">
          <section className="text-center space-y-8 max-w-5xl mx-auto landing-hero">
            
            {/* Crown divider */}
            <div className="crown-divider">
              <span className="crown-divider-line" />
              <CrownIcon style={{filter: 'drop-shadow(0 2px 8px rgba(212,175,55,0.4))'}} />
              <span className="crown-divider-line" />
            </div>

            {/* Subtitle */}
            <p className="landing-subtitle">
              Miss/Master Nkul-Beti – 17<sup>e</sup> édition
            </p>

            {/* Main title with glow */}
            <div className="landing-title">
              <h1 className="text-5xl sm:text-6xl lg:text-7xl font-black text-gray-900 leading-tight">
                Beauté, Élégance
                
                <span className="text-brand">&amp; Excellence</span>
              </h1>
            </div>

            {/* Description */}
            <p className="text-lg sm:text-xl text-gray-700 max-w-3xl mx-auto leading-relaxed px-4">
              Événement officiel <strong className="text-brand font-semibold">organisé par l'Université des Montagne</strong>.
              <br className="hidden sm:block" />
              Découvrez les profils, soutenez vos candidats favoris et votez en toute simplicité.
            </p>

            {/* Call to action buttons */}
            <div className="landing-cta pt-4">
              <a className="btn btn-primary" href="/candidates?category=Miss">
                <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
                </svg>
                Voter Miss
              </a>
              <a className="btn btn-outline" href="/candidates?category=Master">
                <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
                </svg>
                Voter Master
              </a>
            </div>

            {/* Additional info */}
            <div className="pt-8 text-sm text-gray-600 space-y-2">
              <p className="flex items-center justify-center gap-2">
                <svg className="w-4 h-4 text-brand" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clipRule="evenodd" />
                </svg>
                Vote en temps réel • Transparent • Sécurisé
              </p>
            </div>

          </section>
        </main>
      </div>
    </>
  )
}