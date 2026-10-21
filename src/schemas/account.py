from pydantic import BaseModel, ConfigDict

from src.schemas.transaction import TransactionResponse


class AccountBase(BaseModel):
    account_number: str


class AccountCreate(AccountBase):
    pass


class AccountResponse(AccountBase):
    id: int
    balance: float
    user_id: int

    model_config = ConfigDict(from_attributes=True)


class StatementResponse(BaseModel):
    account_number: str
    balance: float
    transactions: list[TransactionResponse]

    model_config = ConfigDict(from_attributes=True)