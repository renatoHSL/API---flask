from typing import List

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

# from app.models import Tasks
from base import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(128))
    created_at: Mapped[DateTime] = mapped_column(index=True)
    updated_at: Mapped[DateTime] = mapped_column(index=True)
    tasks: Mapped[List["Tasks"]] = relationship("Tasks", secondary="user_task_association", back_populates="users")
