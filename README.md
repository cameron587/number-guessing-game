README_TEXT = """
# Number Guessing Game 🎯

A simple command-line Python game where you try to guess a randomly chosen number between 1 and 100.

## How to Play

- Run the game with Python:
  python3 number_guessing_game.py
- Enter your name when prompted.
- Guess the number; the game tells you if your guess is too high or too low.
- Keep guessing until you get it right.
- Your score (number of tries) is saved.
- A top 5 leaderboard is displayed after each game.

## Features

- Random number generation between 1 and 100.
- Tracks the number of tries.
- Saves player scores to 'high_scores.txt'.
- Displays top 5 leaderboard.

## Requirements

- Python 3.x installed.

## Author

Cameron McLaren
"""

# Save README.md file (if it doesn't exist yet)
try:
    with open("README.md", "x") as f:
        f.write(README_TEXT)
        print("README.md file created!")
except FileExistsError:
    print("README.md already exists.")

# Print README content
print(README_TEXT)
