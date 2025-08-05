import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import Config
from database import init_db, close_db
from bot import set_bot_commands, set_admin_commands
from handlers.user_handlers import register_user_handlers
from handlers.admin_handlers import register_admin_handlers
from handlers.game_handlers import register_game_handlers

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    """Main function to start the bot"""
    try:
        # Initialize configuration
        config = Config()
        config.validate()
        
        # Initialize database
        await init_db()
        logger.info("Database initialized")
        
        # Initialize bot and dispatcher
        bot = Bot(token=config.BOT_TOKEN)
        storage = MemoryStorage()
        dp = Dispatcher(storage=storage)
        
        # Register handlers
        register_user_handlers(dp)
        register_admin_handlers(dp)
        register_game_handlers(dp)
        
        # Import and register emoji game handlers
        from handlers.emoji_game_handlers import register_emoji_game_handlers
        register_emoji_game_handlers(dp)
        
        # Block all non-command messages to ensure bot only responds to commands and callbacks
        from aiogram import F
        from aiogram.types import Message
        
        async def ignore_non_commands(message: Message):
            """Ignore all messages that are not commands"""
            pass
        
        # This will catch all remaining messages (non-commands) and ignore them
        dp.message.register(ignore_non_commands, ~F.text.startswith("/"))
        
        # Set bot commands
        await set_bot_commands(bot)
        await set_admin_commands(bot, config.ADMIN_IDS)
        
        logger.info("Bot commands set successfully")
        
        # Start polling
        logger.info("Starting bot polling...")
        await dp.start_polling(bot)
        
    except Exception as e:
        logger.error(f"Error starting bot: {e}")
        raise
    finally:
        # Close database connections
        await close_db()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
