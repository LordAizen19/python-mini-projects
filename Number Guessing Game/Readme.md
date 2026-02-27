# Number Guessing Game

A simple command-line guessing game where you try to guess a random number within a limited number of attempts.

## 📋 Project Overview

This game lets you:
- Choose a lower and upper bound
- Guess a random number within the range
- Get hints if your guess is too high or too low
- Play with 7 total attempts

## 📁 Project Structure

```
Number Guessing Game/
├── numbGuess.py     # Game logic and prompts
└── Readme.md        # Project documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system

### Usage

Run the game:
```bash
python3 numbGuess.py
```

Follow the prompts to set the bounds and enter guesses.

## ✨ Gameplay Rules

- You get 7 total guesses.
- If your guess is too high or too low, the game tells you.
- The game ends after the correct guess or when attempts run out.

## 📊 Example Flow

```
Enter the Lower Bound: 1
Enter the Higher Bound: 20
Enter your guessed number: 10
Too Low, Try a higer number
Enter your guessed number: 15
Correct!, The number is 15. You guessed it in 2 attempts
Game Ends
```

