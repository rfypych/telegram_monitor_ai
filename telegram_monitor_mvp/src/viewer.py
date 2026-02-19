import pandas as pd
import time
import os
from .config import OUTPUT_FILE

DASHBOARD_FILE = "dashboard.html"

def generate_html_dashboard():
    """Generates a clean HTML dashboard from the CSV file."""
    if not os.path.exists(OUTPUT_FILE):
        print(f"Waiting for data... ({OUTPUT_FILE} not found)")
        return

    try:
        df = pd.read_csv(OUTPUT_FILE)
        if df.empty:
            print("Data file is empty.")
            return
            
        # Select relevant columns for display
        cols_to_show = [
            "scraped_at", "channel", "item_name", "price_raw", "currency",
            "ai_valuation", "ai_reasoning", "status"
        ]
        
        # Filter existing columns only
        cols = [c for c in cols_to_show if c in df.columns]
        display_df = df[cols].copy()
        
        # Sort by scraped_at descending (newest first)
        if 'scraped_at' in display_df.columns:
            display_df = display_df.sort_values(by='scraped_at', ascending=False)


        # HTML Template
        html_top = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Telegram Monitor Dashboard</title>
            <meta http-equiv="refresh" content="10"> <!-- Auto-refresh every 10s -->
            <style>
                body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f4f9; color: #333; margin: 20px; }
                h1 { color: #2c3e50; text-align: center; }
                .meta { text-align: center; margin-bottom: 20px; color: #7f8c8d; font-size: 0.9em; }
                table { width: 100%; border-collapse: collapse; margin-top: 20px; background: white; box-shadow: 0 1px 3px rgba(0,0,0,0.2); border-radius: 8px; overflow: hidden; }
                th, td { padding: 12px 15px; text-align: left; border-bottom: 1px solid #ddd; }
                th { background-color: #34495e; color: white; text-transform: uppercase; font-size: 0.85em; letter-spacing: 1px; }
                tr:hover { background-color: #f1f1f1; }
                
                /* Valuation Colors */
                .val-good { background-color: #d4efdf; color: #145a32; font-weight: bold; }
                .val-bad { background-color: #fadbd8; color: #7b241c; font-weight: bold; }
                .val-fair { background-color: #fdebd0; color: #9c640c; font-weight: bold; }
                .val-unknown { color: #7f8c8d; }
                .val-error { background-color: #e74c3c; color: white; font-weight: bold; }

                .price { font-family: 'Consolas', monospace; font-weight: bold; color: #2980b9; }
                .refresh-note { text-align: center; margin-top: 20px; font-size: 0.8em; color: #95a5a6; }
                .channel-tag { background-color: #3498db; color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.8em; }
            </style>
        </head>
        <body>
            <h1>🤖 Telegram Monitor & AI Valuation</h1>
        """
        
        html_middle = f"""
            <div class="meta">
                Last Updated: {time.strftime('%Y-%m-%d %H:%M:%S')} | 
                Total Items Scraped: <strong>{len(df)}</strong> | 
                Source: {OUTPUT_FILE}
            </div>
            <table>
                <thead>
                    <tr>
                        <th style="width: 15%">Time</th>
                        <th style="width: 15%">Channel</th>
                        <th style="width: 25%">Item Name</th>
                        <th style="width: 10%">Price</th>
                        <th style="width: 10%">Valuation</th>
                        <th style="width: 25%">Reasoning</th>
                    </tr>
                </thead>
                <tbody>
        """
        
        rows_html = ""
        for _, row in display_df.head(100).iterrows(): # Show top 100 recent
            # Valuation Logic for Styling
            val_text = str(row.get('ai_valuation', 'Unknown'))
            val_lower = val_text.lower()
            
            row_class = ""
            if 'good' in val_lower or 'deal' in val_lower: row_class = "val-good"
            elif 'overpriced' in val_lower: row_class = "val-bad"
            elif 'fair' in val_lower: row_class = "val-fair"
            elif 'error' in val_lower: row_class = "val-error"
            else: row_class = "val-unknown"

            rows_html += f"""
                    <tr>
                        <td style="font-size: 0.9em; color: #7f8c8d;">{str(row.get('scraped_at', ''))[:19]}</td>
                        <td><span class="channel-tag">{row.get('channel', 'Unknown')}</span></td>
                        <td><strong>{row.get('item_name', 'N/A')}</strong></td>
                        <td class="price">{row.get('price_raw', 'N/A')} {row.get('currency', '')}</td>
                        <td class="{row_class}">{val_text}</td>
                        <td style="font-size: 0.9em;">{row.get('ai_reasoning', '')}</td>
                    </tr>
            """
            
        html_bottom = """
                </tbody>
            </table>
            <div class="refresh-note">
                Dashboard auto-refreshes every 10 seconds. Keep the python script running.
            </div>
        </body>
        </html>
        """

        full_html = html_top + html_middle + rows_html + html_bottom

        with open(DASHBOARD_FILE, "w", encoding="utf-8") as f:
            f.write(full_html)
        
        print(f"Dashboard updated: {os.path.abspath(DASHBOARD_FILE)} ({len(df)} items)")

    except Exception as e:
        print(f"Error generating dashboard: {e}")

def main():
    print(f"Starting Dashboard Generator...")
    print(f"Reading from: {OUTPUT_FILE}")
    print(f"Writing to:   {DASHBOARD_FILE}")
    print("-" * 50)
    
    while True:
        generate_html_dashboard()
        time.sleep(10)

if __name__ == "__main__":
    main()
