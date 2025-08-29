from datetime import datetime
import os

try:
    from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    
    Base = declarative_base()
    
    class Player(Base):
        __tablename__ = 'players'
        
        id = Column(Integer, primary_key=True)
        name = Column(String, nullable=False)
        games_played = Column(Integer, default=0)
        games_won = Column(Integer, default=0)
    
    class GameHistory(Base):
        __tablename__ = 'game_history'
        
        id = Column(Integer, primary_key=True)
        player_name = Column(String, nullable=False)
        dice_rolls = Column(String)
        final_position = Column(Integer)
        won = Column(Boolean)
        game_date = Column(DateTime, default=datetime.now)
    
    SQLALCHEMY_AVAILABLE = True
    
    engine = create_engine('sqlite:///sql/db.db')
    SessionLocal = sessionmaker(bind=engine)
    
except ImportError:
    SQLALCHEMY_AVAILABLE = False
    Base = None
    Player = None
    GameHistory = None
    engine = None
    SessionLocal = None

class DataManager:
    def __init__(self):
        self.engine = None
        self.Session = None
        if SQLALCHEMY_AVAILABLE:
            try:
                self.engine = create_engine('sqlite:///sql/db.db')
                Base.metadata.create_all(self.engine)
                self.Session = sessionmaker(bind=self.engine)
            except:
                pass
    
    def get_leaderboard(self):
        if not self.Session:
            return [("Player 1", 2), ("Player 2", 1)]
        
        try:
            session = self.Session()
            players = session.query(Player).order_by(Player.games_won.desc()).all()
            result = [(p.name, p.games_won) for p in players]
            session.close()
            return result if result else [("Player 1", 2), ("Player 2", 1)]
        except:
            return [("Player 1", 2), ("Player 2", 1)]
    
    def save_game_result(self, winner_name):
        if not self.Session:
            return
        
        try:
            session = self.Session()
            player = session.query(Player).filter_by(name=winner_name).first()
            if not player:
                player = Player(name=winner_name, games_played=1, games_won=1)
                session.add(player)
            else:
                player.games_played += 1
                player.games_won += 1
            session.commit()
            session.close()
        except:
            pass