# Miss/Master Voting Frontend (Next.js + Tailwind)

## Quick start
```bash
# 1) Install deps
npm install

# 2) Configure backend API
cp .env.local.example .env.local
# (default points to http://127.0.0.1:8000)

# 3) Run
npm run dev
# open http://localhost:3000
```

Pages:
- `/` Landing with CTA buttons
- `/candidates` Grid of Miss/Master (tabs)
- `/candidate/[slug]` Detail + Pay & Vote form
- `/success` Confirmation page

The app reads candidates from your backend:
- GET `${NEXT_PUBLIC_API_BASE}/api/candidates/`
- GET `${NEXT_PUBLIC_API_BASE}/api/candidates/<slug>/`
- POST `${NEXT_PUBLIC_API_BASE}/api/vote-intents/`
- GET `${NEXT_PUBLIC_API_BASE}/api/vote-intents/<id>/`
