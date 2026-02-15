import re

def extract_product_info(text):
    """
    Extracts structured information from a raw Telegram message.
    """
    if not text:
        return None

    lines = text.strip().split('\n')
    item_name = lines[0].strip()[:100]

    # Improved Regex for Price
    # 1. Look for explicit "Price: ..." pattern
    explicit_price_pattern = r'(?i)(?:price|harga|bin)\s*[:\-\s]+\s*([^\n]+)'
    explicit_match = re.search(explicit_price_pattern, text)

    price_raw = "N/A"
    currency = "Unknown"

    if explicit_match:
        price_raw = explicit_match.group(1).strip()
    else:
        # 2. Fallback: Look for currency symbols directly (00, Rp 50000)
        currency_pattern = r'(?i)($\s*\d[\d.,kK]*|Rp\s*\d[\d.,]*|\d[\d.,]*\s*(?:USD|IDR|USDT))'
        currency_match = re.search(currency_pattern, text)
        if currency_match:
            price_raw = currency_match.group(1).strip()

    # Determine currency from the extracted price string
    if '$' in price_raw or 'USD' in price_raw.upper():
        currency = 'USD'
    elif 'Rp' in price_raw or 'IDR' in price_raw.upper():
        currency = 'IDR'
    elif 'USDT' in price_raw.upper():
        currency = 'USDT'

    # Status
    status = "Available"
    if re.search(r'(?i)(sold|laku|taken)', text):
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
        "[SOLD] PS5 Digital Edition\n00",
        "Cheap VPS 4GB RAM\nPrice: 10 USDT per month"
    ]
    for s in samples:
        print(f"Input: {s.splitlines()[0]}")
        print(f"Parsed: {extract_product_info(s)}")
        print("-" * 30)
