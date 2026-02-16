import re

def extract_product_info(text):
    """
    Extracts structured information from a raw Telegram message.
    """
    if not text:
        return None

    lines = text.strip().split('\n')
    item_name = lines[0].strip()[:100]

    price_raw = "N/A"
    currency = "Unknown"

    # 1. Look for explicit keywords "Price:", "Harga:", "Mahar:", "BIN:"
    explicit_price_pattern = r'(?i)(?:price|harga|mahar|bin|net)\s*[:\-\s]+\s*([^\n]+)'
    explicit_match = re.search(explicit_price_pattern, text)

    if explicit_match:
        price_raw = explicit_match.group(1).strip()
    else:
        # 2. Fallback: Search for currency patterns directly
        # Improved to catch: 50k, 50rb, 100USD, Rp50.000

        # Matches numbers followed by optional k/rb/jt/currency
        strong_pattern = r'(?i)($\s*\d[\d.,]*[kK]?|Rp\s*\d[\d.,]*[kKrbjt]*|\d[\d.,]*\s*(?:USD|IDR|USDT|rb|jt|k|K)\b)'

        matches = re.search(strong_pattern, text)
        if matches:
            price_raw = matches.group(1).strip()

    # Determine currency & Clean up
    if price_raw != "N/A":
        lower_price = price_raw.lower()
        if '$' in price_raw or 'usd' in lower_price:
            currency = 'USD'
        elif 'rp' in lower_price or 'idr' in lower_price or 'rb' in lower_price or 'jt' in lower_price:
            currency = 'IDR'
        elif 'usdt' in lower_price:
            currency = 'USDT'
        elif 'k' in lower_price:
            # Assume IDR if 'k' is used in loose context, but this is ambiguous
            pass

    # Status
    status = "Available"
    if re.search(r'(?i)(sold|laku|taken|close)', text):
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
        "Jual akun Netflix Premium\nHarga Rp 50.000 / bulan",
        "[SOLD] PS5 Digital Edition\nMahar 4.5jt nego",
        "Cheap VPS 4GB RAM\n10 USDT per month",
        "Jual Akun ML Mythic\n50k aja fast",
        "Promo Joki Tugas\nMulai 50rb"
    ]
    for s in samples:
        print(f"Input: {s.splitlines()[0]}")
        print(f"Parsed: {extract_product_info(s)}")
        print("-" * 30)
