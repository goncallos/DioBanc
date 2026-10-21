# DioBanc 💳

Sistema de API bancária assíncrona desenvolvido em Python com FastAPI, SQLAlchemy 2.0 e Poetry.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.13**
* **FastAPI**: Framework web moderno e assíncrono para construção de APIs.
* **SQLAlchemy 2.0**: ORM assíncrono para modelação e persistência de dados.
* **Asyncpg / Greenlet**: Conector assíncrono para base de dados PostgreSQL.
* **Pydantic**: Validação rigorosa de esquemas e serialização de dados.
* **Poetry**: Gestor de dependências e ambientes virtuais.
* **Uvicorn**: Servidor ASGI de alta performance.
* **Passlib (Bcrypt) & Python-Jose**: Hash de senhas e geração de tokens JWT (OAuth2).

---

## 📁 Estrutura do Projeto

```text
DioBanc/
├── alembic/              # Ficheiros de migração de base de dados
├── src/
│   ├── models/           # Entidades da base de dados (User, Account, Transaction)
│   ├── routers/          # Endpoints da API (auth, accounts, transactions)
│   ├── schemas/          # Schemas de validação Pydantic
│   ├── services/         # Regras de negócio e autenticação
│   ├── config.py         # Carregamento de variáveis de ambiente
│   ├── database.py       # Configuração da sessão e motor assíncrono
│   ├── dependencies.py   # Injeção de dependências (Current User via JWT)
│   └── main.py           # Ponto de entrada da aplicação FastAPI
├── tests/                # Testes automatizados da API
├── .env                  # Variáveis de ambiente
├── pyproject.toml        # Metadados e dependências do Poetry
└── README.md             # Documentação do projeto

📖 Documentação da API
Após inicializar a aplicação, aceda aos seguintes links no navegador:

Swagger UI (Interativo): http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

📌 Principais Funcionalidades e Endpoints
🔐 Autenticação (/auth)
POST /auth/register — Registo de novo utilizador.

POST /auth/login — Autenticação de utilizador com devolução de token JWT.

🏦 Contas Bancárias (/accounts)
POST /accounts/ — Abertura de conta corrente para o utilizador autenticado.

GET /accounts/{account_number}/statement — Consulta de extrato com histórico completo de transações e saldo atual.

💸 Transações (/transactions)
POST /transactions/{account_number}/deposit — Depósito de saldo em conta.

POST /transactions/{account_number}/withdraw — Levantamento de saldo com validação de fundos disponíveis.