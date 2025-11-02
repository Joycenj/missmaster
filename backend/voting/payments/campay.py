# voting/payments/campay.py
import os, time
import requests

CAMPAY_API_BASE = os.getenv("CAMPAY_API_BASE", "https://api.campay.net").rstrip("/")
CAMPAY_KEY = os.getenv("CAMPAY_KEY", "")
CAMPAY_SECRET = os.getenv("CAMPAY_SECRET", "")

# If your CamPay account uses different paths, override these with env vars
CAMPAY_TOKEN_PATH = os.getenv("CAMPAY_TOKEN_PATH", "/token/")          # e.g. /token/
CAMPAY_COLLECT_PATH = os.getenv("CAMPAY_COLLECT_PATH", "/collect/")    # e.g. /collect/
CAMPAY_STATUS_PATH = os.getenv("CAMPAY_STATUS_PATH", "/transaction/")  # e.g. /transaction/{reference}/

class CampayError(Exception):
    pass

def _token():
    """
    Obtain a short-lived access token from CamPay using your key/secret.
    """
    if not CAMPAY_KEY or not CAMPAY_SECRET:
        raise CampayError("CAMPAY_KEY / CAMPAY_SECRET not configured")

    url = f"{CAMPAY_API_BASE}{CAMPAY_TOKEN_PATH}"
    # Many gateways use JSON body for client credentials; adjust if your account requires form-encoded.
    payload = {"username": CAMPAY_KEY, "password": CAMPAY_SECRET}
    # Alternatives you may see in docs: {"client_id": ..., "client_secret": ...} or {"api_key": ..., "api_secret": ...}
    r = requests.post(url, json=payload, timeout=30)
    if r.status_code >= 400:
        raise CampayError(f"Token error {r.status_code}: {r.text}")
    data = r.json()
    # Common shapes: {"token": "..."} or {"access_token": "..."}
    token = data.get("token") or data.get("access_token")
    if not token:
        raise CampayError(f"Token missing in response: {data}")
    return token

def _auth_headers():
    return {"Authorization": f"Token {_token()}"}
    # Some tenants use "Bearer <token>" instead of "Token <token>". If you see 401, change to:
    # return {"Authorization": f"Bearer {_token()}"}

def request_collect(reference: str, amount: int, currency: str, payer_phone: str, provider: str, description: str):
    """
    Ask CamPay to collect money from user's wallet (MTN/Orange).
    On success, CamPay should push a payment prompt to the user's phone.
    Returns a dict containing gateway reference(s).
    """
    url = f"{CAMPAY_API_BASE}{CAMPAY_COLLECT_PATH}"
    body = {
        "amount": amount,
        "currency": currency,          # e.g. "XAF"
        "from": payer_phone,           # user's wallet MSISDN
        "provider": provider,          # "MTN" or "ORANGE" if your tenant requires it; some tenants infer
        "reference": reference,        # your own unique ref to correlate (our VoteIntent.payment_ref)
        "description": description[:128]
    }
    r = requests.post(url, json=body, headers=_auth_headers(), timeout=60)
    if r.status_code >= 400:
        raise CampayError(f"Collect error {r.status_code}: {r.text}")
    return r.json()

def check_status(reference: str):
    """
    Optional: poll transaction status by your reference.
    Some tenants expose /transaction/<reference>/ or /collect/<reference>/status.
    We keep the base path configurable via CAMPAY_STATUS_PATH.
    """
    path = CAMPAY_STATUS_PATH.rstrip("/")
    # If it already includes a placeholder, format it; else append
    if "{reference}" in path:
        url = f"{CAMPAY_API_BASE}{path}".format(reference=reference)
    else:
        url = f"{CAMPAY_API_BASE}{path}/{reference}/"
    r = requests.get(url, headers=_auth_headers(), timeout=30)
    if r.status_code >= 400:
        raise CampayError(f"Status error {r.status_code}: {r.text}")
    return r.json()
