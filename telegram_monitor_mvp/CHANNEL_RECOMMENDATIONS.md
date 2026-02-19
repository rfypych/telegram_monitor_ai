# Recommended Channels to Monitor

This system is designed to detect **Price** and **Item Name**. Therefore, this script works best on the following types of channels:

## 1. Marketplace / Classifieds / FJB
Channels where people post items for sale with a clear format.
*   **Keywords**: "Marketplace", "Buy Sell Trade", "Classifieds", "Hardware Swap".
*   **Why?**: Posts usually contain standard formats like "For Sale: ...", "Price: $...", "Condition: ...". Our Regex is very accurate here.
*   **Examples**: Used Electronics, Game Accounts, Laptops, Sneakers.

## 2. Freelance & Job Boards
Freelance job posting channels, especially those listing a *budget*.
*   **Keywords**: "Freelance Jobs", "Hiring Developers", "Remote Work", "Gig Economy".
*   **Why?**: Often contain text like "Budget: 00" or "Rate: 0/hr". The script will capture this as the "Price".

## 3. P2P Crypto & Exchangers
Channels for peer-to-peer crypto or digital currency trading.
*   **Keywords**: "P2P Exchange", "WTS USDT", "OTC Crypto".
*   **Why?**: The format is very rigid, e.g., "WTS 100 USDT Rate 1.01". The script can easily capture the numbers and currency.

## 4. Deals & Discounts
Channels that share discount information.
*   **Keywords**: "Deals", "Discounts", "Price Drops".
*   **Why?**: The bot can track price changes or promo prices posted by admins.

---

## How to Find These Channels

Use the Search feature in the Telegram app with keywords:
1.  `@marketplace...`
2.  `@buy_sell...`
3.  `@freelance...`
4.  `@crypto_otc...`

Or search on Telegram directory websites like [Telegram Channels](https://tgstat.com/).

## Best Message Format for Detection

This script works best with formats like this:

> **Selling iPhone 13**  (First line becomes Item Name)
> Condition: Mint
> **Price: 50** (Has keyword "Price:" or currency symbol "$")
> Location: NY

If a channel only contains chat/discussion without price figures, this script will mark items as "Unpriced".
