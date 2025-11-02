import { useEffect, useState } from "react";
import Nav from "@/components/Nav";
import { listCandidates } from "@/components/Api";

export default function Candidates(){
  const [tab, setTab] = useState("Miss");
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);

  async function load(category){
    setLoading(true);
    try{
      const data = await listCandidates(category);
      setItems(data);
    } finally {
      setLoading(false);
    }
  }
  useEffect(()=>{ load(tab); }, [tab]);

  return (
    <>
      <Nav/>
      <main className="container py-12 page-transition">
        
        {/* Header Section */}
        <div className="flex flex-col sm:flex-row items-center justify-between gap-6 mb-10">
          <div className="flex-1">
            <h1 className="text-4xl sm:text-5xl font-bold text-gray-900 mb-2">
              Nos <span className="text-brand">Candidats</span>
            </h1>
            <p className="text-gray-600">
              Découvrez tous les participants et votez pour votre favori
            </p>
          </div>
          
          {/* Tab Navigation */}
          <div className="flex gap-3">
            {["Miss","Master"].map(name => (
              <button 
                key={name}
                onClick={()=>setTab(name)}
                className={`btn transition-all duration-300 ${
                  tab===name 
                    ? "btn-primary shadow-xl" 
                    : "btn-outline opacity-70 hover:opacity-100"
                }`}
              >
                <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  {name === "Miss" ? (
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
                  ) : (
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
                  )}
                </svg>
                {name}
              </button>
            ))}
          </div>
        </div>

        {/* Back Home Link */}
        <div className="mb-8">
          <a href="/" className="inline-flex items-center text-sm font-medium text-gray-600 hover:text-brand transition-colors">
            <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
            Retour à l'accueil
          </a>
        </div>

        {/* Loading State */}
        {loading && (
          <div className="flex flex-col items-center justify-center py-20">
            <div className="relative w-16 h-16 mb-4">
              <div className="absolute inset-0 border-4 border-gray-200 rounded-full"></div>
              <div className="absolute inset-0 border-4 border-transparent border-t-brand rounded-full animate-spin"></div>
            </div>
            <p className="text-gray-600 font-medium">Chargement des candidats...</p>
          </div>
        )}

        {/* Empty State */}
        {!loading && items.length===0 && (
          <div className="text-center py-20">
            <div className="mb-6">
              <svg className="w-20 h-20 mx-auto text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" />
              </svg>
            </div>
            <h3 className="text-xl font-semibold text-gray-700 mb-2">Aucun candidat disponible</h3>
            <p className="text-gray-500">Les candidats seront bientôt ajoutés. Revenez plus tard!</p>
          </div>
        )}

        {/* Candidates Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
          {items.map((c, idx) => (
            <a 
              key={c.id} 
              href={`/candidate/${c.slug}`} 
              className="card group"
              style={{
                animation: `fadeInUp 0.5s ease-out ${idx * 0.1}s backwards`
              }}
            >
              {/* Image Container */}
              <div className="relative overflow-hidden bg-gray-100">
                <img 
                  src={c.photo_src || c.photo_url} 
                  alt={c.display_name} 
                  className="w-full h-72 object-cover"
                />
                {/* Overlay on hover */}
                <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-black/0 to-black/0 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                  <div className="absolute bottom-4 left-4 right-4">
                    <div className="flex items-center justify-between text-white">
                      <span className="text-sm font-medium">Voir le profil</span>
                      <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                      </svg>
                    </div>
                  </div>
                </div>
                {/* Vote badge */}
                <div className="absolute top-4 right-4 bg-white/95 backdrop-blur-sm rounded-full px-3 py-1.5 shadow-lg">
                  <div className="flex items-center gap-1.5">
                    <svg className="w-4 h-4 text-brand" fill="currentColor" viewBox="0 0 20 20">
                      <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                    </svg>
                    <span className="text-sm font-bold text-gray-800">{c.votes_count}</span>
                  </div>
                </div>
              </div>

              {/* Card Content */}
              <div className="card-content">
                <h3 className="font-bold text-lg text-gray-900 mb-1 group-hover:text-brand transition-colors">
                  {c.display_name}
                </h3>
                {c.short_description && (
                  <p className="text-sm text-gray-600 line-clamp-2 leading-relaxed">
                    {c.short_description}
                  </p>
                )}
                
                {/* Vote CTA */}
                <div className="mt-4 pt-4 border-t border-gray-100">
                  <div className="flex items-center justify-between text-sm">
                    <span className="text-gray-500 font-medium">Cliquez pour voter</span>
                    <svg className="w-5 h-5 text-brand group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
                    </svg>
                  </div>
                </div>
              </div>
            </a>
          ))}
        </div>

        {/* Results count */}
        {!loading && items.length > 0 && (
          <div className="mt-12 text-center">
            <p className="text-gray-600">
              <span className="font-semibold text-brand">{items.length}</span> candidat{items.length > 1 ? 's' : ''} dans la catégorie <span className="font-semibold">{tab}</span>
            </p>
          </div>
        )}

      </main>
    </>
  )
}