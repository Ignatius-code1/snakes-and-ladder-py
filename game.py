import random
from board import Board

class Game:
    def _init_(self, players):
        self.board = Board()
        self.players = players
        self.current_player_index = 0
        self.game_over = False
        self.winner = None

    def roll_dice(self):
        return random.randint(1, 6)

    def get_current_player(self):
        return self.players[self.current_player_index]  
    
    def move_player(self, dice_roll):
    
        player = self.get_current_player()
        new_position = player.position + dice_roll
        
        if new_position > self.board.size:
            return player.position
        
        final_position = self.board.get_new_position(new_position)
        player.position = final_position
        
        return final_position
    
    def check_winner(self):

        player = self.get_current_player()
        if player.position >= self.board.size:
            self.game_over = True
            self.winner = player
            return True
        return False