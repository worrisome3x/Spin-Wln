# Overview

This is a comprehensive Telegram casino bot built with Python using the aiogram framework. The bot provides emoji-based casino games including slots, dice, bowling, darts, basketball, soccer, blackjack, and mines. Users start with $0 balance and can only tip if they have funds. Admins (Owner ID: 7116825344, Developer ID: 5113373557) can add balance to users. The bot only responds to commands and on-screen interactions, ignoring all other messages to prevent interference between users' games.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Bot Framework
- **aiogram**: Modern async Telegram bot framework for handling messages, commands, and callback queries
- **Finite State Machine (FSM)**: Manages game flow states (selecting game, risk level, bet amount, playing)
- **Rate Limiting**: Prevents spam with configurable request limits per user per time window
- **Command System**: Separate command sets for regular users and administrators

## Database Layer
- **SQLAlchemy with AsyncPG**: Async ORM for PostgreSQL database interactions
- **Connection Pooling**: Uses NullPool for simplified connection management in serverless environments
- **Auto-migration**: Automatic table creation on startup
- **Models**: User profiles, game results, transactions, bot statistics, and house balance tracking

## Game Engine
- **Multiple Game Types**: Slots, dice, bowling, darts, basketball, soccer, and roulette with unique mechanics
- **Risk-based Multipliers**: Four risk levels (Low, Medium, High, Extreme) with different payout multipliers
- **Randomized Results**: Game outcomes generated using Python's random module with specific probability distributions
- **Balance Management**: Real-time balance updates with transaction logging

## Security & Controls
- **Admin Authorization**: Role-based access control with owner and developer privileges
- **User Management**: Ban/unban functionality with database persistence
- **Rate Limiting**: Per-user request throttling to prevent abuse
- **Input Validation**: Bet amount limits and user existence checks
- **Transaction Logging**: Complete audit trail for all balance changes

## State Management
- **Memory Storage**: Uses aiogram's MemoryStorage for FSM state persistence during user sessions
- **Session Context**: Maintains game state between user interactions
- **Decorator Pattern**: Reusable decorators for common checks (user existence, rate limiting, admin authorization)

# External Dependencies

## Primary Services
- **PostgreSQL Database**: User data, game results, transactions, and system statistics storage
- **Redis**: Session caching and rate limiting data (configured but not actively used in current implementation)

## Cryptocurrency Integration
- **Bitcoin RPC**: Direct blockchain interaction for Bitcoin transactions
- **Ethereum RPC**: Web3 connectivity for Ethereum-based transactions
- **USDT Contract**: Tether (USDT) smart contract integration for stablecoin payments

## Infrastructure
- **Telegram Bot API**: Core messaging and interaction platform via aiogram framework
- **Environment Variables**: Configuration management for tokens, database URLs, and API endpoints
- **Logging System**: Python's built-in logging for debugging and monitoring
- **System Monitoring**: psutil integration for server health checks and performance metrics