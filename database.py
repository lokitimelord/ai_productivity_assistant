# database.py

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL (SQLite)
DATABASE_URL = "sqlite:///./tasks.db"

# Create the engine to connect to the SQLite database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a base class for declarative models
Base = declarative_base()

# Task model
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# Create a sessionmaker function to interact with the database
def get_db():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create the database tables (if not already created)
Base.metadata.create_all(bind=engine)
