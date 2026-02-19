# Testing Guide: Live Mode (Real Telegram)

Congratulations! Since you now have your `API_ID` and `API_HASH`, you can run this bot with real Telegram data.

## Step 1: Insert Secret Keys

1.  Open the file named `.env` inside the project folder.
2.  Find the lines for `API_ID` and `API_HASH`.
3.  Replace the default text with the codes from my.telegram.org.

Correct Example:
```env
API_ID=12345678
API_HASH=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
SESSION_NAME=my_monitor_session
TARGET_CHANNELS=@some_market,@crypto_signals
GROQ_API_KEY=gsk_... (Leave blank if you don't have one)
BACKFILL_LIMIT=50
```

> **Important**: Do not use quotes (`"` or `'`) unless the code contains spaces (rare).

## Step 2: Run the Script

Open your terminal/command prompt in the `telegram_monitor_mvp` folder, then type:

```bash
python -m src.monitor
```

## Step 3: Login (One Time Only)

Since this is the first time you are connecting the script to your Telegram account, it will ask for verification:

1.  **Please enter your phone (or bot token):**
    Type your phone number with country code (e.g., `+1234567890`), then press Enter.

2.  **Please enter the code you received:**
    Check your Telegram app on your phone (usually sent by "Telegram Service Notification"). Enter that numeric code in the terminal, then press Enter.

3.  **Signed in successfully as ...**
    If successful, the bot will start backfilling history and monitoring the channels listed in `.env`!

## Additional Tips

*   **Session File**: After a successful login, a new file named `my_monitor_session.session` will appear. Do not delete this file so you don't have to login again every time.
*   **Security**: Never share your `.session` file or the contents of `.env` with anyone.
*   **FloodWait Error**: If you login/logout too often or fetch data too quickly, Telegram might temporarily block requests (FloodWait). If this happens, wait a few minutes/hours before trying again.

Good luck!
