from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

SERVER_URL = "mysql+pymysql://root:admin@localhost"

engine_server = create_engine(SERVER_URL)

with engine_server.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS viagens_api"))
    conn.commit()

DATABASE_URL = "mysql+pymysql://root:admin@localhost/viagens_api"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()