import re

def extract_product_info(text):
    """
    Extracts structured information from a raw Telegram message.
    Optimized for International Markets (USD, EUR, Crypto).
    """
    if not text:
        return None

    lines = text.strip().split('\n')
    item_name = lines[0].strip()[:100]

    price_raw = "N/A"
    currency = "Unknown"

    # 1. Look for explicit keywords "Price:", "BIN:", "Cost:", "Budget:"
    explicit_price_pattern = r'(?i)(?:price|bin|cost|budget|ask)\s*[:\-\s]+\s*([^\n]+)'
    explicit_match = re.search(explicit_price_pattern, text)

    if explicit_match:
        price_raw = explicit_match.group(1).strip()
    else:
        # 2. Fallback: Search for currency patterns directly
        # Patterns: 00, 100 USD, 50k (generic), 100 USDT, €50

        # Matches:
        # - Symbol at start: 00, €50, £50
        # - Number + Currency: 100 USD, 100 EUR
        # - Number + k (thousands): 50k
        strong_pattern = r'(?i)([$€£]\s*\d[\d.,]*[kK]?|\d[\d.,]*\s*(?:USD|EUR|GBP|USDT|ETH|BTC|k|K)\b)'

        matches = re.search(strong_pattern, text)
        if matches:
            price_raw = matches.group(1).strip()

    # Determine currency & Clean up
    if price_raw != "N/A":
        lower_price = price_raw.lower()
        if '$' in price_raw or 'usd' in lower_price:
            currency = 'USD'
        elif '€' in price_raw or 'eur' in lower_price:
            currency = 'EUR'
        elif '£' in price_raw or 'gbp' in lower_price:
            currency = 'GBP'
        elif 'usdt' in lower_price:
            currency = 'USDT'
        elif 'eth' in lower_price:
            currency = 'ETH'
        elif 'btc' in lower_price:
            currency = 'BTC'
        # 'k' without symbol is ambiguous, defaulting to Unknown/USD context usually

    # Status Detection
    status = "Available"
    if re.search(r'(?i)(sold|taken|closed|out of stock)', text):
        status = "Sold"

    return {
        "item_name": item_name,
        "price_raw": price_raw,
        "currency": currency,
        "status": status,
        "raw_text": text
    }

if __name__ == "__main__":
    samples = [
        "Selling iPhone 13 Pro Max\nPrice: 50\nCondition: Good",
        "WTS MacBook Air M1\nBIN: 700 USD\nDm me",
        "Netflix Premium Account\nCost: 5 USD / month",
        "[SOLD] PS5 Digital Edition\n00",
        "Cheap VPS 4GB RAM\n10 USDT per month",
        "Selling 100k Gold WoW\nPrice: 50 EUR",
        "Hiring Python Dev\nBudget: 500k (ambiguous)"
    ]
    for s in samples:
        print(f"Input: {s.splitlines()[0]}")
        print(f"Parsed: {extract_product_info(s)}")
        print("-" * 30)
