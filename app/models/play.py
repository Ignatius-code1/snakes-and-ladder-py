import sys
sys.path.append('../..')
from app import Base, engine
from sqlalchemy import Column,String,BIGINT,DateTime,func

class Player(Base):

    __tablename__="player"

    id=Column(BIGINT,primary_key=True,autoincrement=True)
    player_name=Column(String,nullable=False,unique=True)
    dice_play=Column(String,nullable=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now())

if __name__ == "__main__":
    print("Creating tables in Supabase...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")