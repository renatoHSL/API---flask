from sqlalchemy import create_engine

DATABASE_URL = "sqlite+pysqlite:///:memory:"

engine = create_engine(DATABASE_URL, echo=True)

