class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
    
    def move(self, steps):
        self.position = self.position + steps
    
    def reset(self):
        self.position = 0
    
    def get_status(self):
        if self.position == 0:
            return f"{self.name} is at the start"
        elif self.position >= 100:
            return f"{self.name} has won the game!"
        else:
            return f"{self.name} is at position {self.position}"