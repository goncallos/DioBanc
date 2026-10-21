from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

from src.models.transaction import TransactionType


class TransactionCreate(BaseModel):
    amount: float = Field(..., gt=0, description="O montante tem de ser superior a zero")


class TransactionResponse(BaseModel):
    id: int
    amount: float
    transaction_type: TransactionType
    created_at: datetime
    account_id: int

    model_config = ConfigDict(from_attributes=True)