# post-api

Lightweight FastAPI sample for managing posts and users.

## Project layout

```bash
post-api/
├── app/
│   ├── controller/
│   │   ├── __init__.py
│   │   ├── postController.py
│   │   └── userController.py
│   │
│   ├── DB/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── postData.py
│   │
│   ├── model/
│   │   ├── __init__.py
│   │   └── tableModel.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── postRoutes.py
│   │   └── userRoutes.py
│   │
│   ├── schema/
│   │   ├── __init__.py
│   │   ├── postModel.py
│   │   └── userSchema.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   └── utils.py
│   │
│   ├── .env
│   └── server.py
│
├── .gitignore
├── README.md
└── requirements.txt

```


## Features

- CRUD endpoints for posts and basic user routes
- JSON request/response using Pydantic schemas (app/schema/)
- Simple DB layer and session provider (app/DB/database.py)
- OpenAPI docs (Swagger & ReDoc)
- Small, easy-to-read structure suitable for demos and learning

## Quick start (local)

1. Clone repository
2. Create and activate virtualenv:
   - python -m venv .venv
   - Windows: .venv\Scripts\activate
   - macOS / Linux: source .venv/bin/activate
3. Install dependencies:
   - pip install -r requirements.txt
4. Run the app:
   - uvicorn app.server:app --reload --host 0.0.0.0 --port 8000
5. Browse docs:
   - Swagger: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Configuration

- app/.env (loaded by app/DB/database.py using python-dotenv)
- Required env vars (as used in the example database setup):
  - USERNAME — DB username
  - PASSWORD — DB password
  - DATABASE — database name
  - (Host is set to localhost in the example; change the URL if needed)
- Common env var:
  - PORT (default 8000)

## API (summary)

Typical routes exposed by app/routes:

- Posts

  - GET /posts — list posts
  - GET /posts/{id} — retrieve a post
  - POST /posts — create a post
  - PUT /posts/{id} — update a post
  - DELETE /posts/{id} — delete a post

- Users
  - POST /users — create a user
    - Request model: app.schema.userSchema.CreateUser
    - Response model: app.schema.userSchema.UserResp (status 201)
    - Controller: app.controller.create_users
    - Example error: 500 if user creation fails
  - GET /users/{id} — retrieve a user
    - Response model: app.schema.userSchema.UserResp (status 200)
    - Controller: app.controller.retrive_user
    - Example error: 404 if user not found

The user router uses dependency injection for DB sessions (Depends(get_db)), async controller calls, and raises HTTPException for error cases. See app/routes/userRoutes.py for the exact implementation.

## Database / Persistence

This project includes a simple SQLAlchemy setup in app/DB/database.py. It:

- Loads env variables from app/.env using python-dotenv
- Builds a PostgreSQL URL in the form:
  postgresql://USERNAME:PASSWORD@localhost/DATABASE
- Creates an Engine, a SessionLocal (sessionmaker), and a declarative Base
- Exposes a get_db() generator to provide DB sessions via Depends()

Example (conceptual) contents of app/DB/database.py:

```py
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # app/
ENV_PATH = os.path.join(BASE_DIR, '.env')
load_dotenv(ENV_PATH, override=True)

SQL_ALCHEMY_DB_URL = f"postgresql://{os.getenv('USERNAME')}:{os.getenv('PASSWORD')}@localhost/{os.getenv('DATABASE')}"

engine: Engine = create_engine(SQL_ALCHEMY_DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

Notes:

- Update .env with USERNAME, PASSWORD, DATABASE before running.
- If you want a different DB host/port or a connection pool config, modify SQL_ALCHEMY_DB_URL/create_engine accordingly.
- Use Base to declare ORM models in app/model/tableModel.py.

## Testing

- Run tests (if present):
  - pytest

Manual testing: curl, httpie, Postman, or the interactive docs.

## Docker

Build and run (if a Dockerfile exists):

- docker build -t post-api .
- docker run -p 8000:8000 --env-file app/.env post-api

## Contributing

- Open an issue or PR
- Follow existing style and add tests for new behavior

## License

Add a LICENSE file to the repository. If none provided, treat as sample/demo code.
