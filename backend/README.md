# Miss/Master Voting Backend v1.1 (Admin photo upload)

## What's new
- **Admin can add**: name, **short description**, bio, and **upload a picture** (ImageField).
- Media served at `http://127.0.0.1:8000/media/...` in DEBUG.
- API now returns `photo_src` (uploaded photo URL if present, otherwise `photo_url`).

## Quick start
```bash
python -m venv .venv
# Windows PowerShell
. .\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt
copy .env.example .env   # or cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit Admin: http://127.0.0.1:8000/admin/
- Add Category (Miss, Master)
- Add Campaign (set price per vote)
- Add Candidate (fill **display_name**, **short_description**, optional **bio**, then **upload photo** or set **photo_url**)

Public API:
- `GET /api/candidates/` → includes `photo_src`
- `GET /api/candidates/<slug>/` → includes `photo_src`

> On production, configure a real media storage (S3/Cloudinary). For local dev, files are saved into `./media/`.
