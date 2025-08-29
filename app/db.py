from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base,sessionmaker
from dotenv import load_dotenv
import os



load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    print("Warning: DATABASE_URL not found in .env file")
    print("Current working directory:", os.getcwd())
    DATABASE_URL = "postgresql+psycopg2://postgres.cydvkcsxohvtnimatdnm:RyTwbfIMHaAbgGug@aws-0-eu-north-1.pooler.supabase.com:5432/postgres"

engine=create_engine(DATABASE_URL,echo=False,future=True)


SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

#BASE
Base=declarative_base()