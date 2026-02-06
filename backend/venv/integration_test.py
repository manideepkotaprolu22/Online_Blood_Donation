from main import app, get_db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base
import pytest
from fastapi.testclient import TestClient

db_url = "sqlite:///./test.db"
engine = create_engine(db_url, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autoflush=False, autocommit = False,bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def client():
    return TestClient(app)