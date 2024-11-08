from typing import List

from sqlalchemy import func, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from base import Base


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False, index=True)
    description: Mapped[str] = mapped_column(String(128))
    status: Mapped[bool] = mapped_column(index=True)
    created_date: Mapped[DateTime] = mapped_column(insert_default=func.now(), index=True)
    users: Mapped[List["Users"]] = relationship("Users", secondary="user_task_association", back_populates="tasks")
