import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.main import app
from app.database import Base, get_db

# Database in-memory SQLite
SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fixture database session
@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

# Fixture client FastAPI
@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()
    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()

# Fixture untuk auto register + login + dapat token
@pytest.fixture
def auth_client(client):
    # Register user
    client.post("/api/register", json={
        "name": "Test User",
        "email": "testuser@example.com",
        "password": "testpass"
    })
    # Login user
    response = client.post("/api/login", json={
        "email": "testuser@example.com",
        "password": "testpass"
    })
    token = response.json()["data"]["access_token"]
    return {"client": client, "token": token}
