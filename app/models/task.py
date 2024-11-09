from typing import List
from datetime import datetime

from sqlalchemy import func, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False, index=True)
    description: Mapped[str] = mapped_column(String(128), nullable=False)
    status: Mapped[bool] = mapped_column(index=True)
    created_date: Mapped[datetime] = mapped_column(insert_default=func.now(), index=True)
    users: Mapped[List["Users"]] = relationship("Users", secondary="users_tasks_association", back_populates="tasks")
