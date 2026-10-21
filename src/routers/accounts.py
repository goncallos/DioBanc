from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.dependencies import get_current_user
from src.models import User
from src.schemas import AccountCreate, AccountResponse, StatementResponse
from src.services import create_account, get_account_statement

router = APIRouter(prefix="/accounts", tags=["Contas Bancárias"])


@router.post("/", response_model=AccountResponse, status_code=status.HTTP_201_CREATED)
async def open_account(
    account_in: AccountCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await create_account(db, current_user.id, account_in.account_number)


@router.get("/{account_number}/statement", response_model=StatementResponse)
async def read_statement(
    account_number: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await get_account_statement(db, account_number, current_user.id)