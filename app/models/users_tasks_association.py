from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column

from .base import Base


class UserTaskAssociation(Base):
    __tablename__ = "users_tasks_association"

    user_id = mapped_column(ForeignKey("users.id"), primary_key=True)
    task_id = mapped_column(ForeignKey("tasks.id"), primary_key=True)

#  Opção com PrimaryKeyConstraint
# __table_args__ = (PrimaryKeyConstraint("user_id", "task_id"),)