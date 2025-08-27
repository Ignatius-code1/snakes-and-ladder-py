

from game import Game
from .player import Player
from database.db import DataManager

class CLI:
    def __init__(self):
        self.players= []

    def start(self):
        print("\n" + "="*40)
        print("Welcome to the Snakes and Ladders Game!")
        print ("="*40)

        self.setup_players()

        while True:
            print("\n What would you like to do?")
            print("1  Play a new game")
            print("2  View scoreboard")
            print("3  Quit")

            choice = input(" Enter 1, 2, or 3: ").strip()

            if choice == "1":
                self.play_game()
            elif choice == "2":
                self.view_leaderboard()
            elif choice == "3":
                print(" Thanks for playing! See you next time!")
                break
            else:
                print(" Please enter 1, 2, or 3.")

    def setup_players(self):
        print("\n👥 This is a 2-player game: Player 1 vs Player 2")

        self.players = [
            Player("Player 1"),
            Player("Player 2")
        ]

        print(" The players are ready:")
        print("  🟢 Player 1")
        print("  🔵 Player 2")
        print("\nLet the dice roll! First to 100 wins!")

    def play_game(self):
        print("\n Game starting now!")
        game = Game([Player(p.name) for p in self.players])

        while not game.is_game_over():
            game.play_turn()
            input("\n Press Enter to continue...")