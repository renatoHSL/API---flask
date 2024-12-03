from app.db.config import Session
from app.models.users import Users

session = Session()

# Inserir usuário de teste
new_user = Users(username="testuser", email="test@example.com", password_hash="hashed_password")
session.add(new_user)
session.commit()

# Recuperar o usuário
user = session.query(Users).filter_by(username="testuser").first()
print(user.username, user.email)

session.close()
