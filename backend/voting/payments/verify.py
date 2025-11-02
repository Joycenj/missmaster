import os, hmac, hashlib
WEBHOOK_SECRET = os.getenv("CAMPAY_WEBHOOK_SECRET", "")
def valid_signature(raw_body: bytes, header_sig: str) -> bool:
    if not header_sig or not WEBHOOK_SECRET:
        return False
    mac = hmac.new(WEBHOOK_SECRET.encode(), raw_body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(mac, header_sig)
