def encode(data: str) -> str:
    return data.encode().hex()

def decode(data: str) -> str:
    try:
        return bytes.fromhex(data).decode(errors="ignore")
    except ValueError:
        return "❌ Invalid hex input"
