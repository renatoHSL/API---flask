from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from base import Base


class UserTaskAssociation(Base):
    __tablename__ = "user_task_association"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(ForeignKey("users.id"))
    task_id = mapped_column(ForeignKey("tasks.id"))
