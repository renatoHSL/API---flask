import pytest
from app.models.config import Session
from datetime import datetime
from app.models.users import Users
from sqlalchemy import select


def test_insert():
    with Session() as session:
        new_user = Users(username="testuser", email="test@user.com", password_hash="password")
        session.add(new_user)
        session.commit()

        retrieve_user = session.select(Users).filter_by(username="testuser").first()
        print("Created at", retrieve_user.created_at)

        assert retrieve_user.created_at is not None, "Usuário não encontrado"
        assert isinstance(retrieve_user.created_at, datetime)

test_insert()
