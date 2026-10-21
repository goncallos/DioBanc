from fastapi import FastAPI

from src.routers import accounts, auth, transactions

app = FastAPI(
    title="DioBanc - API Bancária Assíncrona",
    description="Sistema bancário assíncrono desenvolvido com FastAPI e SQLAlchemy 2.0.",
    version="0.1.0",
)

app.include_router(auth.router)
app.include_router(accounts.router)
app.include_router(transactions.router)


@app.get("/", tags=["Health Check"])
async def root():
    return {"status": "online", "message": "API DioBanc a funcionar perfeitamente"}