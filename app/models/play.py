
from app import Base, engine
from sqlalchemy import Column,String,BIGINT,DateTime,func

class Player(Base):

    __tablename__="player"

    id=Column(BIGINT,primary_key=True,autoincrement=True)
    player_name=Column(String,nullable=False,unique=True)
    dice_play=Column(String,nullable=False)
    

