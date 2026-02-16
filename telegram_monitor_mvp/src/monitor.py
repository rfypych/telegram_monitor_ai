import asyncio
import os
import random
import time
from telethon import TelegramClient, events
from dotenv import load_dotenv

from .config import API_ID, API_HASH, SESSION_NAME, TARGET_CHANNELS, OUTPUT_FILE, BACKFILL_LIMIT
from .parser import extract_product_info
from .exporter import Exporter
from .ai_valuation import get_valuation

# Setup Exporter
exporter = Exporter(OUTPUT_FILE)

async def process_message(raw_text, channel_name, msg_id):
    """
    Common processing logic for both Listener and Mock modes.
    """
    try:
        # Avoid cluttering logs with every single processing line if bulk parsing
        # print(f"[{channel_name}] Processing: {raw_text.splitlines()[0]}...")

        # 1. Parse Data (Regex)
        parsed_data = extract_product_info(raw_text)

        if parsed_data:
            # Add metadata
            parsed_data['channel'] = channel_name
            parsed_data['message_id'] = msg_id

            # 2. Add AI Valuation (Optional / Mocked if no key)
            if parsed_data.get('price_raw') != "N/A":
                print(f"   -> Analyzing with Groq AI: {parsed_data['item_name']} @ {parsed_data['price_raw']}")
                valuation = get_valuation(
                    item_name=parsed_data['item_name'],
                    price_raw=parsed_data['price_raw'],
                    currency=parsed_data['currency'],
                    raw_text=raw_text
                )
                parsed_data.update(valuation)
            else:
                parsed_data['ai_valuation'] = "N/A"
                parsed_data['ai_reasoning'] = "No price found."

            # 3. Save to CSV
            exporter.save_message(parsed_data)
            print(f"[{channel_name}] Saved: {parsed_data['item_name']}")

    except Exception as e:
        print(f"Error processing message: {e}")

async def message_handler(event):
    """Callback for real Telegram messages."""
    raw_text = event.raw_text
    channel_name = event.chat.title if event.chat else "Unknown Channel"
    msg_id = event.id
    await process_message(raw_text, channel_name, msg_id)

async def backfill_history(client):
    """Fetches historical messages from target channels."""
    print(f"\n--- Starting Backfill ({BACKFILL_LIMIT} messages per channel) ---")
    for channel in TARGET_CHANNELS:
        if not channel: continue
        try:
            print(f"Backfilling from: {channel}...")
            async for message in client.iter_messages(channel, limit=BACKFILL_LIMIT):
                if message.text:
                    channel_name = message.chat.title if message.chat else channel
                    await process_message(message.text, channel_name, message.id)
        except Exception as e:
            print(f"Error backfilling {channel}: {e}")
    print("--- Backfill Complete ---\n")

async def start_listener():
    """Starts the real Telegram listener."""
    print("Starting Telegram Monitor...")
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
    await client.start()

    # 1. Backfill first
    await backfill_history(client)

    # 2. Then listen for new messages
    @client.on(events.NewMessage(chats=TARGET_CHANNELS))
    async def handler(event):
        await message_handler(event)

    print(f"Listening for NEW messages on channels: {TARGET_CHANNELS}")
    await client.run_until_disconnected()

async def start_mock_mode():
    """Simulates receiving messages for testing/demo purposes."""
    print("\n" + "="*50)
    print("   DEMO / MOCK MODE ACTIVATED")
    print("   (Running without API keys for demonstration)")
    print("="*50 + "\n")

    # Simulate Backfill in Mock Mode
    print("--- Simulating Backfill ---")
    mock_history = [
        "WTS Old Item 1\nPrice: 0",
        "WTS Old Item 2\nPrice: 0"
    ]
    for msg in mock_history:
        await process_message(msg, "Mock History Channel", 100)
        await asyncio.sleep(0.1)
    print("--- Backfill Complete ---\n")

    mock_channels = ["Marketplace 1", "Crypto Signals", "Job Board"]
    mock_messages = [
        "WTS iPhone 14 Pro Max 256GB\nPrice: 00\nCondition: Mint\nDM me",
        "Looking for Python dev\nBudget: 00\nContact: @user123",
        "[SOLD] MacBook Air M2\n50",
        "Jual Akun Google Cloud\nRp 150.000 via Dana/OVO",
        "Selling 100 USDT for PayPal F&F\nRate 1:1",
        "Sewa RDP Windows 8GB RAM\nHarga: 50k / bulan"
    ]

    while True:
        await asyncio.sleep(random.uniform(2, 5))

        # Pick random message
        raw_text = random.choice(mock_messages)
        channel = random.choice(mock_channels)
        msg_id = random.randint(1000, 9999)

        await process_message(raw_text, channel, msg_id)

def main():
    # Load config explicitly to check if API_ID is set
    from .config import API_ID

    if not API_ID:
        print("API Credentials not found in .env. Starting Mock Mode...")
        try:
            asyncio.run(start_mock_mode())
        except KeyboardInterrupt:
            print("\nStopped.")
    else:
        try:
            asyncio.run(start_listener())
        except Exception as e:
            print(f"Error starting listener: {e}")
            print("Falling back to Mock Mode for demo...")
            asyncio.run(start_mock_mode())

if __name__ == "__main__":
    main()
