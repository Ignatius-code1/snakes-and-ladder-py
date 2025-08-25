import random
from board import Board

class Game:
    def __init__(self, players):
        self.board = Board()
        self.players = players
        self.current_player_index = 0
        self.game_over = False
        self.winner = None
    
    def roll_dice(self):
        """Roll a six-sided dice"""
        return random.randint(1, 6)
    
    def get_current_player(self):
        """Get the current player"""
        return self.players[self.current_player_index]
    
    def move_player(self, dice_roll):
        """Move current player and handle snakes/ladders"""
        player = self.get_current_player()
        new_position = player.position + dice_roll
        
        # Don't move beyond board size
        if new_position > self.board.size:
            return player.position
        
        # Check for snakes or ladders
        final_position = self.board.get_new_position(new_position)
        player.position = final_position
        
        return final_position
    
    def check_winner(self):
        """Check if current player has won"""
        player = self.get_current_player()
        if player.position >= self.board.size:
            self.game_over = True
            self.winner = player
            return True
        return False
    
    def next_turn(self):
        """Move to next player's turn"""
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
    
    def play_turn(self):
        """Execute one complete turn"""
        if self.game_over:
            return None
        
        player = self.get_current_player()
        dice_roll = self.roll_dice()
        old_position = player.position
        new_position = self.move_player(dice_roll)
        
        # Check for win condition
        won = self.check_winner()
        
        turn_info = {
            'player': player,
            'dice_roll': dice_roll,
            'old_position': old_position,
            'new_position': new_position,
            'won': won
        }
        
        if not won:
            self.next_turn()
        
        return turn_info
    
    def reset_game(self):
        """Reset game to initial state"""
        for player in self.players:
            player.position = 0
        self.current_player_index = 0
        self.game_over = False
        self.winner = None