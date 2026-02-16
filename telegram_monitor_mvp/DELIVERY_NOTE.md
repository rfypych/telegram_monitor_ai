# Delivery Note: Telegram Monitor & Valuation MVP

## Overview
This package contains the Minimum Viable Product (MVP) for the Telegram Channel Monitor with AI Valuation support.

## Key Features Implemented
1.  **Multi-Channel Monitoring**: Tracks multiple public Telegram channels simultaneously.
2.  **Historical Backfill**: Automatically fetches the last 50 (configurable) messages upon startup before switching to live mode.
3.  **Smart Parsing**: Extracts item names, prices, and currency using Regex.
4.  **AI Valuation**: Integrates with **Groq AI** to provide instant valuation ("Good Deal" / "Overpriced") and reasoning.
    *   *Note*: Used Groq for its incredible speed and cost-efficiency (free tier available), as requested for a low-budget MVP.
5.  **CSV Export**: Automatically saves all data to `telegram_data.csv`.

## Startup Instructions
1.  Install dependencies: `pip install -r requirements.txt`
2.  Configure `.env` (see `.env.example`).
3.  Run: `python -m src.monitor`

## Notes for Future Development
*   **Parser**: Currently uses strict rules to ensure accuracy. Can be upgraded to LLM-based parsing for unstructured messages later.
*   **AI**: Currently configured for Groq. Can be swapped for OpenAI/Gemini easily if needed.

## Deliverables
*   Source Code (`src/`)
*   Documentation (`README.md`, `PROPOSAL.md`)
*   Testing Guide (`PANDUAN_TESTING.md` - localized for initial testing)

Ready for deployment.
