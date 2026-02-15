import asyncio
import os
import random
import time
from telethon import TelegramClient, events
from dotenv import load_dotenv

from .config import API_ID, API_HASH, SESSION_NAME, TARGET_CHANNELS, OUTPUT_FILE
from .parser import extract_product_info
from .exporter import Exporter

# Setup Exporter
exporter = Exporter(OUTPUT_FILE)

async def message_handler(event):
    """Callback for new messages."""
    try:
        raw_text = event.raw_text
        channel_name = event.chat.title if event.chat else "Unknown Channel"
        msg_id = event.id

        print(f"[{channel_name}] New Message: {raw_text[:50]}...")

        # Parse data
        parsed_data = extract_product_info(raw_text)
        if parsed_data:
            parsed_data['channel'] = channel_name
            parsed_data['message_id'] = msg_id

            # Save to CSV
            exporter.save_message(parsed_data)

    except Exception as e:
        print(f"Error processing message: {e}")

async def start_listener():
    """Starts the real Telegram listener."""
    print("Starting Telegram Monitor...")
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

    # Register handler
    @client.on(events.NewMessage(chats=TARGET_CHANNELS))
    async def handler(event):
        await message_handler(event)

    print(f"Listening on channels: {TARGET_CHANNELS}")
    await client.start()
    await client.run_until_disconnected()

async def start_mock_mode():
    """Simulates receiving messages for testing/demo purposes."""
    print("\n" + "="*50)
    print("   DEMO / MOCK MODE ACTIVATED")
    print("   (Running without API keys for demonstration)")
    print("="*50 + "\n")

    mock_channels = ["Marketplace 1", "Crypto Signals", "Job Board"]
    mock_messages = [
        "WTS iPhone 14 Pro Max 256GB\nPrice: $900\nCondition: Mint\nDM me",
        "Looking for Python dev\nBudget: $500\nContact: @user123",
        "[SOLD] MacBook Air M2\n$850",
        "Jual Akun Google Cloud\nRp 150.000 via Dana/OVO",
        "Selling 100 USDT for PayPal F&F\nRate 1:1",
        "Sewa RDP Windows 8GB RAM\nHarga: 50k / bulan"
    ]

    while True:
        # Simulate random delay
        await asyncio.sleep(random.uniform(2, 5))

        # Pick random message
        raw_text = random.choice(mock_messages)
        channel = random.choice(mock_channels)

        print(f"[{channel}] New Message (MOCKED): {raw_text.splitlines()[0]}...")

        # Parse
        parsed_data = extract_product_info(raw_text)
        if parsed_data:
            parsed_data['channel'] = channel
            parsed_data['message_id'] = random.randint(1000, 9999)

            # Save
            exporter.save_message(parsed_data)

def main():
    if not API_ID or not API_HASH:
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
