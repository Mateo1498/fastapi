from http import client
import imp
import json
from re import I, T
import pytest
from typing_extensions import override
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app
from app import models, schemas
from app.config import settings
from app.database import get_db
from app.database import Base
from alembic import command

# SQLALCHEMY_DATABSE_URL = f'postgresql://postgres:152346789@loaclhost:5432/fastapi_test'

SQLALCHEMY_DATABSE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABSE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base.metadata.create_all(bind=engine)

# Base = declarative_base()

#def override_get_db():
#    db = TestingSessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()

#def get_db():
#    db = TestingSessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()

#app.dependency_overrides[get_db] = override_get_db

#client = TestClient(app)

@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    