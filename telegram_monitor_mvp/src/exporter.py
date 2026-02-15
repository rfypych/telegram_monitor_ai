import os
import pandas as pd
from datetime import datetime

class Exporter:
    def __init__(self, output_file):
        """
        Initialize the exporter.

        Args:
            output_file (str): Path to the CSV file.
        """
        self.output_file = output_file

    def save_message(self, message_data):
        """
        Save a single message to the CSV file.

        Args:
            message_data (dict): Dictionary containing parsed message data.
        """
        # Add timestamp
        message_data['scraped_at'] = datetime.now().isoformat()

        df = pd.DataFrame([message_data])

        # Append to CSV if exists, else create new
        if os.path.exists(self.output_file):
            df.to_csv(self.output_file, mode='a', header=False, index=False)
        else:
            df.to_csv(self.output_file, mode='w', header=True, index=False)

        print(f"[Exporter] Saved item: {message_data.get('item_name', 'Unknown')}")

if __name__ == "__main__":
    # Test
    exporter = Exporter("test_output.csv")
    exporter.save_message({"item_name": "Test Item 1", "price_raw": "00", "currency": "USD", "status": "Available"})
    exporter.save_message({"item_name": "Test Item 2", "price_raw": "Rp 50.000", "currency": "IDR", "status": "Available"})
    print("Export complete. Check test_output.csv")
