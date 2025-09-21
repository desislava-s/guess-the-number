# 🎮 Guess the Number
A simple Python console game where the player tries to guess the number randomly chosen by the computer.
## Project Goals

- **Practice Python basics**
  - Work with variables, loops, conditionals, and functions.
  - Get comfortable with `input()`, `print()`, and the `random` module.

- **Implement game logic**
  - Generate a random secret number.
  - Compare user guesses with the secret number.
  - Provide feedback (*too high*, *too low*, *correct*).
    
- **Learn GitHub basics**
  - Create a repository and add the project.
  - Write a clear README file.
  - Understand version control for small projects.
## Solution Overview

### Technologies Used
- **Python 3** → main programming language.
- **Built-in `random` module** → generates the secret number.

### Tools Used
- **IDE**: PyCharm
- **GitHub** → host the repository and share the project.

## How It Works
1. The program picks a random number between 1 and 100.
2. The player enters guesses in the console.
3. The game compares the guess with the secret number:
   - Too low → print "Too low!"
   - Too high → print "Too high!"
   - Correct → print "Correct!"
4. The loop continues until the player guesses correctly.
5. The program displays how many attempts it took.

---

## How to Run

1. Make sure you have **Python 3** installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/desislava-s/guess-the-number.git
