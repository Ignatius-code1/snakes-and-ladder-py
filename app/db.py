from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base,sessionmaker
from dotenv import load_dotenv
import os



load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine=create_engine(DATABASE_URL,echo=False,future=True)


SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

#BASE
Base=declarative_base()