from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from base import Base


class UserTaskAssociation(Base):
    __tablename__ = "user_task_association"

    user_id = mapped_column(ForeignKey("users.id"), primary_key=True)
    task_id = mapped_column(ForeignKey("tasks.id"), primary_key=True)
