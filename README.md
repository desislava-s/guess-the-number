# 🎮 Guess the Number
A simple Python console game where the player tries to guess the number randomly chosen by the computer.
## 🎯 Project Goals

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
## 🛠️ Solution Overview

### 🔹 Technologies Used
- **Python 3** → main programming language.
- **Built-in `random` module** → generates the secret number.

### 🔹 Tools Used
- **IDE**: PyCharm
- **GitHub** → host the repository and share the project.

### 🔹 How It Works
1. The program picks a random number between 1 and 100.
2. The player enters guesses in the console.
3. The game compares the guess with the secret number:
   - Too low → print "Too low!"
   - Too high → print "Too high!"
   - Correct → print "Correct!"
4. The loop continues until the player guesses correctly.
5. The program displays how many attempts it took.

**New Features**:  
   - **Restart option** → after finishing a game, the player can decide to play again or exit.  
   - **Guess counter** → the game tracks how many attempts were needed to find the number and displays it in the winning message.  
   - **Levels with increasing difficulty** →  
     - Level 1 starts with range `1–100`.  
     - Each time the player guesses correctly, the level increases and the range expands by +25 (Level 2: 1–125, Level 3: 1–150, etc.).  
     - The player can continue to the next level or quit.  

This setup makes the game progressively more challenging and keeps the player engaged.

---

## 🚀 How to Run

1. Make sure you have **Python 3** installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/desislava-s/guess-the-number.git

## 📄 Screenshots
<img width="488" height="250" alt="image" src="https://github.com/user-attachments/assets/e11cd4cf-8b5e-43ed-847e-59f97ea8a20b" />
<img width="631" height="243" alt="image" src="https://github.com/user-attachments/assets/580d4583-87c4-4faa-98a6-d2c294cf7965" />
<img width="537" height="195" alt="image" src="https://github.com/user-attachments/assets/459ff246-ed65-451e-a856-a4aac588f01b" />


## 📂 Source Code

 [Source code](guess_the_number.py)

## 📝 Changelog
- v1.3: Added levels - after each win, the player advances to a higher level with a larger number range.
- v1.2: Added guess counter - game now shows how many attempts the player needed to guess the number.
- v1.1: Added restart option so players can play multiple rounds in a row.
- v1.0: Initial version of the game.


