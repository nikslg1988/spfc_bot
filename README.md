# spfc_bot
# CPFC Bot --- Calorie & Food Control

Telegram bot for calculating daily calorie intake and performing
qualitative food analysis using LLM (DeepSeek).

The project is built with clean architecture principles and clear
separation of responsibilities.

------------------------------------------------------------------------

## Features

-   User registration via FSM (height, weight, age, gender, activity,
    goal)
-   Daily calorie calculation (Mifflin--St Jeor formula)
-   LLM-based qualitative food analysis
-   Inline keyboard UX
-   Error-safe LLM integration (fallback mechanism)
-   Fully asynchronous architecture

------------------------------------------------------------------------

## Architecture

    Telegram (aiogram)
       ↓
    FSM (validation & state management)
       ↓
    Business services (pure logic)
       ↓
    LLM adapter (DeepSeek via aiohttp)
       ↓
    PostgreSQL (planned)

### Design Principles

-   FSM validates input only
-   Services contain pure business logic
-   LLM never performs strict calculations
-   Handlers orchestrate only
-   LLM errors never break the bot (fallback always returned)
-   Database will be the source of truth (FSM is temporary storage)

------------------------------------------------------------------------

## Tech Stack

-   Python 3.11+
-   aiogram 3.x
-   aiohttp
-   DeepSeek API
-   PostgreSQL (in progress)
-   asyncpg (planned)

------------------------------------------------------------------------

## Project Structure

    handlers/
    states/
    services/
        calories.py
        llm/
    keyboards/
    mappers/
    db/ (planned)
    config.py
    main.py

------------------------------------------------------------------------

## Setup

### 1. Clone repository

``` bash
git clone <repo_url>
cd cpfc_bot
```

### 2. Create virtual environment

``` bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Create config.py

``` python
BOT_TOKEN = "your_telegram_bot_token"
DEEPSEEK_API_KEY = "your_deepseek_api_key"
```

`config.py` must be added to `.gitignore`.

------------------------------------------------------------------------

## Run

``` bash
python main.py
```

------------------------------------------------------------------------

## Current Status

-   ✅ User registration flow
-   ✅ Daily calorie calculation service
-   ✅ LLM integration for food analysis
-   🔄 PostgreSQL integration
-   🔜 Persistent food logs and daily statistics

------------------------------------------------------------------------

## Future Improvements

-   Database persistence (users, food logs)
-   Daily aggregation logic
-   REST API (FastAPI)
-   Dockerization
-   Deployment setup
