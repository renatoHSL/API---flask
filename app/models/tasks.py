from typing import List
from datetime import datetime

from sqlalchemy import func, String, ForeignKey, Boolean, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


# from app.models import Users


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
    description: Mapped[str] = mapped_column(String(128), nullable=False)
    is_done: Mapped[bool] = mapped_column(Boolean, default=False, index=True)
    created_date: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now(), index=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now(), onupdate=func.now(), index=True)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    # TODO Possivel importação circular
    # users: Mapped[List["Users"]] = relationship("Users", secondary="users_tasks_association", back_populates="tasks")
