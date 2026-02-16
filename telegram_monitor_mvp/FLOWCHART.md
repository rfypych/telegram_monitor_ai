# System Architecture Flowchart

This flowchart illustrates how the Telegram Monitor processes messages from start to finish.

```mermaid
flowchart TD
    A[Start Script] --> B{"Load Config (.env)"}
    B -->|API Keys Present| C[Connect to Telegram Telethon]
    B -->|Missing Keys| D[Start Mock Mode Simulation]

    C --> E[Historical Backfill]
    E --> F[Fetch Last N Messages]
    F --> G[Process Message]

    E --> H[Start Live Listener]
    H -->|New Message Arrives| G

    G --> I[Parser Regex]
    I -->|Extract Price/Item| J{Valid Price Found?}

    J -->|No| K[Mark as Unpriced]
    J -->|Yes| L{AI Key Present?}

    L -->|No| M[Skip Valuation]
    L -->|Yes| N[Call Groq AI API]
    N -->|Get Valuation| O["Add Good Deal / Overpriced Tag"]

    K --> P[Export to CSV]
    M --> P
    O --> P

    P --> H
    D --> G
```

## Key Components

1.  **Telethon Client**: Handles the connection to Telegram's MTProto servers.
2.  **Backfill Module**: Iterates through message history to capture past data.
3.  **Regex Parser**: Extracts structured data (Price, Currency, Item Name) from unstructured text.
4.  **Groq AI**: Provides intelligent valuation logic (Good Deal vs Bad Deal).
5.  **CSV Exporter**: Appends processed data to a local file for analysis.
