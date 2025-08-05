from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from config import Config

async def set_bot_commands(bot: Bot):
    """Set bot commands menu"""
    commands = [
        BotCommand(command="start", description="🎮 Start the casino bot"),
        BotCommand(command="balance", description="💰 Check your balance"),
        BotCommand(command="games", description="🎯 View available games"),
        BotCommand(command="play", description="🎲 Start a game"),
        BotCommand(command="dice", description="🎲 Roll dice game"),
        BotCommand(command="diceroll", description="🎲 Roll dice (short)"),
        BotCommand(command="dr", description="🎲 Roll dice (shortest)"),
        BotCommand(command="basketball", description="🏀 Basketball game"),
        BotCommand(command="basket", description="🏀 Basketball (short)"),
        BotCommand(command="bowling", description="🎳 Bowling game"),
        BotCommand(command="darts", description="🎯 Darts game"),
        BotCommand(command="soccer", description="⚽ Soccer game"),
        BotCommand(command="slots", description="🎰 Slot machine"),
        BotCommand(command="mines", description="💣 Mines game"),
        BotCommand(command="blackjack", description="🃏 Blackjack game"),
        BotCommand(command="bonus", description="🎁 Daily bonus"),
        BotCommand(command="stats", description="📊 Your statistics"),
        BotCommand(command="leaderboard", description="🏆 Top players"),
        BotCommand(command="tip", description="💝 Tip another user"),
        BotCommand(command="cancel", description="❌ Cancel current game"),
        BotCommand(command="help", description="❓ Help and rules"),
    ]
    
    await bot.set_my_commands(commands)

async def set_admin_commands(bot: Bot, admin_ids: list):
    """Set admin-specific commands"""
    admin_commands = [
        BotCommand(command="admin", description="🔧 Admin panel"),
        BotCommand(command="debug", description="🐛 Debug information"),
        BotCommand(command="health", description="🏥 System health"),
        BotCommand(command="housebal", description="🏦 House balance"),
        BotCommand(command="tip", description="💝 Tip user"),
        BotCommand(command="addbalance", description="➕ Add balance to user"),
        BotCommand(command="drain", description="💧 Drain user balance"), 
        BotCommand(command="ban", description="🚫 Ban user"),
        BotCommand(command="unban", description="✅ Unban user"),
        BotCommand(command="broadcast", description="📢 Broadcast message"),
    ]
    
    for admin_id in admin_ids:
        await bot.set_my_commands(admin_commands, scope={"type": "chat", "chat_id": admin_id})
