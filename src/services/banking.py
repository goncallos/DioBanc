from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.models import Account, Transaction, TransactionType
from src.schemas import StatementResponse, TransactionCreate, TransactionResponse


async def create_account(db: AsyncSession, user_id: int, account_number: str) -> Account:
    query = select(Account).where(Account.account_number == account_number)
    result = await db.execute(query)
    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Número de conta já existente.",
        )

    account = Account(account_number=account_number, user_id=user_id, balance=0.0)
    db.add(account)
    await db.commit()
    await db.refresh(account)
    return account


async def process_transaction(
    db: AsyncSession,
    account_number: str,
    transaction_in: TransactionCreate,
    transaction_type: TransactionType,
    user_id: int,
) -> TransactionResponse:
    query = select(Account).where(
        Account.account_number == account_number, Account.user_id == user_id
    )
    result = await db.execute(query)
    account = result.scalar_one_or_none()

    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conta bancária não encontrada ou não pertence ao utilizador.",
        )

    if transaction_type == TransactionType.WITHDRAW and account.balance < transaction_in.amount:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Saldo insuficiente para efetuar o levantamento.",
        )

    if transaction_type == TransactionType.DEPOSIT:
        account.balance += transaction_in.amount
    elif transaction_type == TransactionType.WITHDRAW:
        account.balance -= transaction_in.amount

    transaction = Transaction(
        amount=transaction_in.amount,
        transaction_type=transaction_type,
        account_id=account.id,
    )
    db.add(transaction)
    await db.commit()
    await db.refresh(transaction)

    return TransactionResponse.model_validate(transaction)


async def get_account_statement(
    db: AsyncSession, account_number: str, user_id: int
) -> StatementResponse:
    query = (
        select(Account)
        .options(selectinload(Account.transactions))
        .where(Account.account_number == account_number, Account.user_id == user_id)
    )
    result = await db.execute(query)
    account = result.scalar_one_or_none()

    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conta não encontrada.",
        )

    return StatementResponse.model_validate(account)