import random

def generate_recommendation(symbol: str) -> dict:
    entry = random.randint(48000, 51000)
    exit_price = entry + random.randint(1000, 3000)
    return {
        "symbol": symbol,
        "confidence": random.randint(80, 95),
        "recommendation": random.choice(["Long", "Short", "Hold"]),
        "entry": entry,
        "exit": exit_price
    }