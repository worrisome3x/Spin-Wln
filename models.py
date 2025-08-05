from datetime import datetime, timezone
from decimal import Decimal
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, Boolean, Text, Numeric, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import enum

Base = declarative_base()

class GameType(enum.Enum):
    SLOT = "slot"
    DICE = "dice"
    BOWLING = "bowling"
    DART = "dart"
    BASKETBALL = "basketball"
    FOOTBALL = "football"
    ROULETTE = "roulette"
    MINES = "mines"
    BLACKJACK = "blackjack"
    DICEROLL = "diceroll"

class TransactionType(enum.Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    GAME_WIN = "game_win"
    GAME_LOSS = "game_loss"
    BONUS = "bonus"
    TIP = "tip"
    ADMIN_ADD = "admin_add"
    ADMIN_DRAIN = "admin_drain"

class RiskLevel(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    EXTREME = "extreme"

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, unique=True, nullable=False, index=True)
    username = Column(String(50), nullable=True)
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)
    balance = Column(Numeric(precision=18, scale=8), default=Decimal('0.0'), nullable=False)
    is_banned = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    last_bonus_date = Column(DateTime, nullable=True)
    total_wagered = Column(Numeric(precision=18, scale=8), default=Decimal('0.0'), nullable=False)
    total_won = Column(Numeric(precision=18, scale=8), default=Decimal('0.0'), nullable=False)
    games_played = Column(Integer, default=0, nullable=False)
    
    # Relationships
    transactions = relationship("Transaction", back_populates="user")
    game_results = relationship("GameResult", back_populates="user")

class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    transaction_type = Column(Enum(TransactionType), nullable=False)
    amount = Column(Numeric(precision=18, scale=8), nullable=False)
    balance_before = Column(Numeric(precision=18, scale=8), nullable=False)
    balance_after = Column(Numeric(precision=18, scale=8), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Foreign key for admin transactions
    admin_id = Column(BigInteger, nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="transactions")

class GameResult(Base):
    __tablename__ = 'game_results'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    game_type = Column(Enum(GameType), nullable=False)
    bet_amount = Column(Numeric(precision=18, scale=8), nullable=False)
    multiplier = Column(Numeric(precision=10, scale=2), nullable=False)
    risk_level = Column(Enum(RiskLevel), nullable=False)
    game_result = Column(Integer, nullable=False)  # Dice value, slot result, etc.
    payout = Column(Numeric(precision=18, scale=8), nullable=False)
    profit = Column(Numeric(precision=18, scale=8), nullable=False)  # payout - bet_amount
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationships
    user = relationship("User", back_populates="game_results")

class HouseBalance(Base):
    __tablename__ = 'house_balance'
    
    id = Column(Integer, primary_key=True)
    balance = Column(Numeric(precision=18, scale=8), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    updated_by = Column(BigInteger, nullable=True)  # Admin ID who updated

class GameSession(Base):
    __tablename__ = 'game_sessions'
    
    id = Column(Integer, primary_key=True)
    creator_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    opponent_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    game_type = Column(Enum(GameType), nullable=False)
    bet_amount = Column(Numeric(precision=18, scale=8), nullable=False)
    status = Column(String(20), default='waiting', nullable=False)  # waiting, active, completed, cancelled
    creator_result = Column(Integer, nullable=True)
    opponent_result = Column(Integer, nullable=True)
    winner_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    completed_at = Column(DateTime, nullable=True)
    
    # Relationships
    creator = relationship("User", foreign_keys=[creator_id])
    opponent = relationship("User", foreign_keys=[opponent_id])

class BotStats(Base):
    __tablename__ = 'bot_stats'
    
    id = Column(Integer, primary_key=True)
    total_users = Column(Integer, default=0, nullable=False)
    total_games_played = Column(Integer, default=0, nullable=False)
    total_wagered = Column(Numeric(precision=18, scale=8), default=Decimal('0.0'), nullable=False)
    total_paid_out = Column(Numeric(precision=18, scale=8), default=Decimal('0.0'), nullable=False)
    house_profit = Column(Numeric(precision=18, scale=8), default=Decimal('0.0'), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
