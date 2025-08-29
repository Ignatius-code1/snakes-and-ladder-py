class DataManager:
    def __init__(self):
        self.scores = {"Player 1": 0, "Player 2": 0}
    
    def get_leaderboard(self):
        return [(name, wins) for name, wins in self.scores.items()]
    
    def save_game_result(self, winner_name):
        if winner_name in self.scores:
            self.scores[winner_name] += 1
        print(f"{winner_name} won! Current scores: {self.scores}")