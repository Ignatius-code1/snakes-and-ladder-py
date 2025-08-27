import random
from board import Board

class Game:
    def _init_(self, players):
        self.board = Board()
        self.players = players
        self.current_player_index = 0
        self.game_over = False
        self.winner = None

        