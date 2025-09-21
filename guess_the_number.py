import random

target_number = random.randint(1, 100)

while True:
    player_input = input("Guess the number (1-100): ")

    if not player_input.isdigit():
        print("Invalid input! Please enter a number between 1 and 100.")
        continue

    player_number = int(player_input)

    if player_number == target_number:
        print("Correct! You guessed the number!")
        break
    elif player_number > target_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
