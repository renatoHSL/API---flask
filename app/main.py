from models.config import Session

with Session().begin() as session:
    session.add(some_object)
    session.add(some_other_object)
