from typing import List

from sqlalchemy import create_engine, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from userTaskAssociation import UserTaskAssociation
from user import Users
from base import Base

DATABASE_URL = "sqlite+pysqlite:///:memory:"

engine = create_engine(DATABASE_URL, echo=True)


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(index=True)
    description: Mapped[str]
    status: Mapped[bool] = mapped_column(index=True)
    created_date: Mapped[DateTime] = mapped_column(insert_default=func.now(), index=True)
    parents: Mapped[List[Users]] = relationship(secondary=UserTaskAssociation, back_populates="children")
