# Telegram Channel Monitor (MVP)

This is a Minimum Viable Product (MVP) for monitoring Telegram channels, parsing product information, and saving it to a CSV file.

## Features

-   **Real-time Listener**: Connects to Telegram via Telethon API.
-   **Mock Mode**: Simulates incoming messages for testing/demo purposes (useful if you don't have API keys yet).
-   **Parser**: Extracts Item Name, Price, Currency, and Status (Available/Sold) using Regex.
-   **Exporter**: Saves parsed data to a CSV file automatically.

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Configuration**:
    -   Copy `.env.example` to `.env`.
    -   Fill in your `API_ID` and `API_HASH` from [my.telegram.org](https://my.telegram.org).
    -   Add target channel usernames.

3.  **Run**:
    ```bash
    python -m src.monitor
    ```

## Mock Mode (Demo)

If you do not provide `API_ID` in the `.env` file, the script will automatically start in **Mock Mode**.
This generates fake Telegram messages and processes them, allowing you to see the parser and CSV exporter in action without needing to connect to Telegram servers.

## Project Structure

-   `src/monitor.py`: Main entry point. Handles Telegram connection or Mock loop.
-   `src/parser.py`: Logic for extracting price/item info.
-   `src/exporter.py`: Logic for saving data to CSV.
-   `src/config.py`: Configuration loader.
