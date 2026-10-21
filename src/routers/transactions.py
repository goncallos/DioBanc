from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.dependencies import get_current_user
from src.models import TransactionType, User
from src.schemas import TransactionCreate, TransactionResponse
from src.services import process_transaction

router = APIRouter(prefix="/transactions", tags=["Transações"])


@router.post("/{account_number}/deposit", response_model=TransactionResponse)
async def deposit(
    account_number: str,
    transaction_in: TransactionCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await process_transaction(
        db, account_number, transaction_in, TransactionType.DEPOSIT, current_user.id
    )


@router.post("/{account_number}/withdraw", response_model=TransactionResponse)
async def withdraw(
    account_number: str,
    transaction_in: TransactionCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await process_transaction(
        db, account_number, transaction_in, TransactionType.WITHDRAW, current_user.id
    )