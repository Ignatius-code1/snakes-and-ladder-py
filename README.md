# Snakes and Ladders Game

A Python implementation of the classic Snakes and Ladders board game with database persistence.

## Features

- **2-Player Game**: Fixed Player 1 vs Player 2 gameplay
- **Interactive CLI**: Menu-driven interface with play/scoreboard/quit options
- **Database Storage**: SQLite database stores player scores and game history
- **Real-time Gameplay**: Dice rolling, snake/ladder mechanics, turn-by-turn display

## Installation

1. Install dependencies:
```bash
pipenv install
```

2. Run the game:
```bash
pipenv run python main.py
```

## How to Play

1. Choose option `1` to start a new game
2. Press Enter to roll dice for each turn
3. First player to reach position 100 wins
4. View scoreboard with option `2`
5. Quit with option `3`

## Game Mechanics

- **Dice**: Random rolls 1-6
- **Snakes**: Move player down the board
- **Ladders**: Move player up the board
- **Winning**: First to reach exactly position 100

## Data Storage

- **Database**: `sql/db.db` (SQLite)
- **Tables**: Players (names, wins) and Game History
- **Persistence**: Scores saved between sessions

## Project Structure

```
├── main.py          # Entry point
├── cli.py           # User interface
├── game.py          # Game logic
├── player.py        # Player class
├── board.py         # Board mechanics
├── app/db.py        # Database management
└── sql/db.db        # SQLite database
```