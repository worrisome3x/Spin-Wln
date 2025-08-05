# Telegram Casino Bot - Spin & Win 🎰

A comprehensive Telegram casino bot with emoji-based games, admin controls, and user balance management.

## Features

### Games Available
- 🎲 **Dice Games** (`/dice`, `/diceroll`, `/dr`)
- 🏀 **Basketball** (`/basketball`, `/basket`) 
- 🎳 **Bowling** (`/bowling`)
- 🎯 **Darts** (`/darts`)
- ⚽ **Soccer** (`/soccer`)
- 🎰 **Slots** (`/slots`)
- 🃏 **Blackjack** (`/blackjack`)
- 💣 **Mines** (`/mines`)

### User Features
- 💰 Balance system (starts at $0)
- 💝 Tip other users (`/tip`)
- 📊 View statistics (`/stats`)
- 🏆 Leaderboards (`/leaderboard`)
- 🎁 Daily bonuses (`/bonus`)

### Admin Features
- ➕ Add balance to users (`/addbalance`)
- 🔧 Admin panel (`/admin`)
- 📊 System health monitoring (`/health`)
- 🏦 House balance management (`/housebal`)

## Bot Information
- **Bot Username**: @spinandwincasinobot
- **Admin Access**: Owner (7116825344) & Developer (5113373557)
- **Security**: Game state isolation, rate limiting, command-only responses

## Deployment

### Environment Variables Required
```
BOT_TOKEN=your_telegram_bot_token
DATABASE_URL=your_postgresql_database_url
```

### Installation
```bash
pip install -r requirements.txt
python main.py
```

### For Render Deployment
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python main.py`
- **Service Type**: Web Service (for 24/7 uptime)

## Database
- PostgreSQL with SQLAlchemy ORM
- Automatic table creation on startup
- BigInteger support for large Telegram user IDs

## Security Features
- Rate limiting per user
- Admin-only commands with ID verification
- User state isolation in games
- Input validation and sanitization

---
Built with aiogram framework for reliable Telegram bot operations.