import os
from dataclasses import dataclass
from typing import List

@dataclass
class Config:
    """Configuration class for the casino bot"""
    
    # Bot Configuration
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    
    # Database Configuration
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/casino_bot")
    
    # Redis Configuration
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    
    # Admin Configuration
    OWNER_ID: int = int(os.getenv("OWNER_ID", "7116825344"))
    DEV_ID: int = int(os.getenv("DEV_ID", "5113373557"))
    
    # Crypto Configuration
    BITCOIN_RPC_URL: str = os.getenv("BITCOIN_RPC_URL", "")
    ETHEREUM_RPC_URL: str = os.getenv("ETHEREUM_RPC_URL", "")
    TETHER_CONTRACT_ADDRESS: str = os.getenv("TETHER_CONTRACT_ADDRESS", "0xdAC17F958D2ee523a2206206994597C13D831ec7")
    
    # Game Configuration
    MIN_BET: float = float(os.getenv("MIN_BET", "0.01"))
    MAX_BET: float = float(os.getenv("MAX_BET", "1000.0"))
    HOUSE_EDGE: float = float(os.getenv("HOUSE_EDGE", "0.02"))  # 2% house edge
    
    # Security Configuration
    RATE_LIMIT_REQUESTS: int = int(os.getenv("RATE_LIMIT_REQUESTS", "30"))  # requests per minute
    RATE_LIMIT_WINDOW: int = int(os.getenv("RATE_LIMIT_WINDOW", "60"))  # seconds
    SESSION_TIMEOUT: int = int(os.getenv("SESSION_TIMEOUT", "1800"))  # 30 minutes
    MAX_CONCURRENT_GAMES: int = int(os.getenv("MAX_CONCURRENT_GAMES", "5"))
    
    # Bonus Configuration
    DAILY_BONUS_AMOUNT: float = float(os.getenv("DAILY_BONUS_AMOUNT", "1.0"))
    WELCOME_BONUS_AMOUNT: float = float(os.getenv("WELCOME_BONUS_AMOUNT", "0.0"))
    
    # Multiplier Configuration
    BASE_MULTIPLIER: float = 1.0
    MAX_MULTIPLIER: float = 50.0
    RISK_MULTIPLIER_LOW: float = 1.2
    RISK_MULTIPLIER_MEDIUM: float = 2.5
    RISK_MULTIPLIER_HIGH: float = 5.0
    RISK_MULTIPLIER_EXTREME: float = 10.0
    
    # House Balance Configuration
    INITIAL_HOUSE_BALANCE: float = 500.0
    MIN_HOUSE_BALANCE: float = 100.0
    
    @property
    def ADMIN_IDS(self) -> List[int]:
        """Get list of admin user IDs"""
        return [self.OWNER_ID, self.DEV_ID]
    
    def validate(self) -> bool:
        """Validate configuration"""
        if not self.BOT_TOKEN:
            raise ValueError("BOT_TOKEN is required")
        if not self.DATABASE_URL:
            raise ValueError("DATABASE_URL is required")
        return True
