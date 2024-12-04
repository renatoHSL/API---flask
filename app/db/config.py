import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

ENV = os.getenv("FLASK_ENV", "development")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Preparação para possivel mudança para postgresql
DATABASE_URL = f"sqlite+pysqlite:///{os.path.join(BASE_DIR, 'data', 'database.db')}" \
    if ENV == "development" \
    else "postgresql://user:pass@localhost/db"

print("aqui esta a url correta", DATABASE_URL)

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
