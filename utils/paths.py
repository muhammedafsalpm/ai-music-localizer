import os

BASE = "data"

def ensure_dirs():
    os.makedirs(f"{BASE}/input", exist_ok=True)
    os.makedirs(f"{BASE}/output", exist_ok=True)