from typing import List
from datetime import datetime

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(128), nullable=False)
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now(), index=True)
    updated_at: Mapped[datetime] = mapped_column(insert_default=func.now(), onupdate=func.now(), index=True)
    tasks: Mapped[List["Tasks"]] = relationship("Tasks", secondary="users_tasks_association", back_populates="users")

    def __repr__(self) -> str:
        return (
            f"Users(id={self.id!r}, username={self.username!r}, email={self.email!r}, "
            f"created_at={self.created_at!r}, updated_at={self.updated_at!r})"
        )
