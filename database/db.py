from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

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

class GameDatabase:
    def __init__(self, supabase_url=None, supabase_key=None):
        if supabase_url and supabase_key:
        
            self.engine = create_engine(f'postgresql://{supabase_url}')
        else:
            
            db_path = os.path.join(os.path.dirname(__file__), 'game.db')
            self.engine = create_engine(f'sqlite:///{db_path}')
        
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    
    def add_player(self, name):
        existing = self.session.query(Player).filter_by(name=name).first()
        if not existing:
            player = Player(name=name)
            self.session.add(player)
            self.session.commit()
    
    def save_game_result(self, player_name, dice_rolls, final_position, won):
        dice_rolls_str = ','.join(map(str, dice_rolls))
        
        game = GameHistory(
            player_name=player_name,
            dice_rolls=dice_rolls_str,
            final_position=final_position,
            won=won
        )
        self.session.add(game)
        
        player = self.session.query(Player).filter_by(name=player_name).first()
        if player:
            player.games_played += 1
            if won:
                player.games_won += 1
        
        self.session.commit()
    
    def get_player_stats(self, name):
        player = self.session.query(Player).filter_by(name=name).first()
        if player:
            return {'games_played': player.games_played, 'games_won': player.games_won}
        return {'games_played': 0, 'games_won': 0}