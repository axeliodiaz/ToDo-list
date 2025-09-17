# ToDo-list

Project to handle a ToDo list app with FastAPI

## Getting started

1) Create your environment file from the example and adjust values if needed:
   - macOS/Linux: `cp .env.example .env`
   - Windows (PowerShell): `Copy-Item .env.example .env`

2) Start the services:
   - `docker compose up --build`

3) Access the API:
   - Base URL: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs

## Environment variables

Environment variables are loaded via docker-compose `env_file: .env`.
A dummy example is provided in `.env.example`. Copy it to `.env` before running the stack.

The following variables are supported:

- POSTGRES_DB: Database name (used by the Postgres container)
- POSTGRES_USER: Database user
- POSTGRES_PASSWORD: Database password
- PORT: Port used by the API inside the container (default 8000)
- DATABASE_URL: Connection string the API uses to talk to Postgres (async, e.g., postgresql+asyncpg://todo_user:todo_password@db:5432/todo_db)

Notes:
- The compose file maps host port 8000 to container port 8000 (`"8000:8000"`). If you change PORT in `.env`, also adjust the compose ports mapping accordingly.
- The API is expected to run with Uvicorn using `app.main:app`.