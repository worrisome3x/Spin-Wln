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
        BotCommand(command="multiplayer", description="👥 Multiplayer games"),
        BotCommand(command="deposit", description="💳 Deposit crypto"),
        BotCommand(command="withdraw", description="💸 Withdraw funds"),
        BotCommand(command="bonus", description="🎁 Daily bonus"),
        BotCommand(command="stats", description="📊 Your statistics"),
        BotCommand(command="leaderboard", description="🏆 Top players"),
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
        BotCommand(command="addbalance", description="➕ Add balance"),
        BotCommand(command="drain", description="💧 Drain balance"),
        BotCommand(command="ban", description="🚫 Ban user"),
        BotCommand(command="unban", description="✅ Unban user"),
        BotCommand(command="broadcast", description="📢 Broadcast message"),
    ]
    
    for admin_id in admin_ids:
        await bot.set_my_commands(admin_commands, scope={"type": "chat", "chat_id": admin_id})
