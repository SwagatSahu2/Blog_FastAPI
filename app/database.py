from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL ="mssql+pyodbc://sa:sa@IN-CVF3NX3/BlogCrudDb?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes"

engine = create_engine(DATABASE_URL, connect_args={"driver": "ODBC Driver 17 for SQL Server"})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base=declarative_base()

