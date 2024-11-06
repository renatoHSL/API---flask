from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from base import Base

DATABASE_URL = "sqlite+pysqlite:///:memory:"

engine = create_engine(DATABASE_URL, echo=True)


class UserTaskAssociation(Base):
    __tablename__ = "user_task_association"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(ForeignKey("users.id"))
    task_id = mapped_column(ForeignKey("tasks.id"))
