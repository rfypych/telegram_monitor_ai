import pandas as pd
import time
import os
from tabulate import tabulate
from .config import OUTPUT_FILE

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_dashboard():
    print("Waiting for data...")
    while True:
        try:
            if os.path.exists(OUTPUT_FILE):
                df = pd.read_csv(OUTPUT_FILE)
                if not df.empty:
                    # Select key columns
                    cols = ["scraped_at", "channel", "item_name", "price_raw", "ai_valuation"]
                    # Get last 10 entries
                    latest = df[cols].tail(10)

                    clear_screen()
                    print(f"=== Telegram Monitor Dashboard (Last 10 Items) ===")
                    print(f"Source: {OUTPUT_FILE}")
                    print(f"Last Update: {time.strftime('%H:%M:%S')}")
                    print("-" * 80)
                    print(tabulate(latest, headers='keys', tablefmt='grid', showindex=False))
                    print("-" * 80)
                    print("Press Ctrl+C to exit.")
            else:
                print(f"File {OUTPUT_FILE} not found yet. Waiting...")

        except Exception as e:
            print(f"Error reading data: {e}")

        time.sleep(5)

if __name__ == "__main__":
    show_dashboard()
