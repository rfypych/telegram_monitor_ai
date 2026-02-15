import os
from groq import Groq
from .config import GROQ_API_KEY, GROQ_MODEL

def get_valuation(item_name, price_raw, currency, raw_text):
    """
    Uses Groq AI to estimate the value of an item.

    Args:
        item_name (str): Name of the item.
        price_raw (str): The raw price string (e.g., "00").
        currency (str): The currency (e.g., "USD").
        raw_text (str): The full text of the listing for context.

    Returns:
        dict: {
            "ai_valuation": "Good Deal" | "Overpriced" | "Fair" | "Unknown",
            "ai_reasoning": "Short explanation..."
        }
    """

    # 1. Check if API Key is present. If not, return a Mock/Dummy response.
    if not GROQ_API_KEY:
        return {
            "ai_valuation": "AI_DISABLED",
            "ai_reasoning": "No Groq API Key found. Add GROQ_API_KEY to .env to enable."
        }

    client = Groq(api_key=GROQ_API_KEY)

    prompt = f"""
    You are an expert appraiser. Analyze this sales listing from a Telegram channel.

    Item: {item_name}
    Price: {price_raw} {currency}
    Full Context: "{raw_text}"

    Task:
    1. Determine if this price is a Good Deal, Fair Market Value, or Overpriced based on general market knowledge.
    2. Provide a very short reasoning (max 1 sentence).

    Output format (strictly 2 lines):
    VALUATION: [Good Deal/Fair/Overpriced/Unknown]
    REASON: [Your short reasoning]
    """

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful valuation assistant. Be concise."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model=GROQ_MODEL,
            temperature=0.2,
            max_tokens=100,
        )

        response = chat_completion.choices[0].message.content.strip()
        lines = response.split('\n')

        valuation = "Unknown"
        reasoning = response

        for line in lines:
            if line.startswith("VALUATION:"):
                valuation = line.replace("VALUATION:", "").strip()
            elif line.startswith("REASON:"):
                reasoning = line.replace("REASON:", "").strip()

        return {
            "ai_valuation": valuation,
            "ai_reasoning": reasoning
        }

    except Exception as e:
        return {
            "ai_valuation": "ERROR",
            "ai_reasoning": f"AI Call Failed: {str(e)}"
        }

if __name__ == "__main__":
    # Test (Mock Mode if no key)
    print("Testing AI Valuation...")
    res = get_valuation("iPhone 13", "00", "USD", "Selling iPhone 13 128GB Mint Condition")
    print(res)
