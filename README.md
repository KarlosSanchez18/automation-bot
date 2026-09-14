# Automation Bot — Web → Telegram Notifications

A small integration service that receives events from a web application and forwards structured notifications to Telegram through a bot.

This repository demonstrates a simple but common integration pattern: **HTTP event → backend validation/processing → external messaging API**.

## What it does

- Receives events through a Flask backend.
- Separates API routes from Telegram-specific logic.
- Sends messages to a configured Telegram chat/channel.
- Loads credentials and configuration from environment variables.
- Keeps sensitive values outside version control.

## Architecture

```text
website / external service
        |
        | HTTP request
        v
     Flask API
        |
        | processed event
        v
 Telegram Bot API
        |
        v
 channel / group
```

## Project structure

```text
automation-bot/
├── app.py
├── config.py
├── requirements.txt
├── .env.example
├── bot/
│   ├── __init__.py
│   └── telegram_bot.py
└── routes/
    ├── __init__.py
    └── api.py
```

## Stack

- Python 3
- Flask
- Telegram Bot API
- Requests
- python-dotenv

## Local setup

```bash
git clone https://github.com/KarlosSanchez18/automation-bot.git
cd automation-bot

python -m venv .venv
```

Activate the virtual environment:

```bash
# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` from the example file:

```env
TELEGRAM_BOT_TOKEN=your_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

Run the service:

```bash
python app.py
```

## Security notes

- Tokens and chat identifiers should stay in environment variables.
- `.env` must not be committed.
- In a production deployment, incoming requests should be authenticated/validated according to the source system.

## Why this project exists

This is a compact public example of the integration work I do in larger systems: receiving events from one service, applying application logic, and handing the result to another platform through an API.

## Author

**Karlos Sanchez** — Full-Stack Developer focused on automation, integrations and business systems.

[LinkedIn](https://www.linkedin.com/in/karlos-sanchez/) · [GitHub profile](https://github.com/KarlosSanchez18)
