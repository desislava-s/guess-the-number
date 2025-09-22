import random

while True:
    target_number = random.randint(1, 100)
    print(target_number)
    attempts_counter = 0
    print("A new number has been chosen between 1 and 100!")

    while True:
        player_input = input("Guess the number (1-100): ")

        if not player_input.isdigit():
            print("Invalid input! Please enter a number between 1 and 100.")
            continue

        player_number = int(player_input)
        attempts_counter += 1

        if player_number == target_number:
            print(f"Correct! You guessed the number in  {attempts_counter} attempts!")
            break
        elif player_number > target_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")

    play_again = input("Do you want to start new game? (y/n): ").lower()

    if play_again != "y":
        print("Thank you for playing! Goodbye!")
        break
