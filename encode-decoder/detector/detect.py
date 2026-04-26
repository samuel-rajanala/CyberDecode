import re

def detect_format(data: str):
    if not data:
        return ["Unknown"]

    results = []

    if re.fullmatch(r'[A-Za-z0-9+/=]+', data) and len(data) % 4 == 0:
        results.append("Base64")

    if re.fullmatch(r'[A-Z2-7=]+', data):
        results.append("Base32")

    if re.fullmatch(r'[0-9a-fA-F]+', data):
        results.append("Hex")

    if re.search(r'%[0-9A-Fa-f]{2}', data):
        results.append("URL")

    return results if results else ["Unknown"]
