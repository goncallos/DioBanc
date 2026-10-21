import enum
from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from src.database import Base


class TransactionType(str, enum.Enum):
    DEPOSIT = "deposito"
    WITHDRAW = "saque"


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    transaction_type = Column(Enum(TransactionType), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)

    account = relationship("Account", back_populates="transactions")