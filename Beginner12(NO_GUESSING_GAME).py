import random
import logo

print(logo.logo)

random_number = random.randint(1,100)

def compare(guess, random_number):
    if guess > random_number:
        return "High"
    else:
        return "low"

def play_game():
    difficulty = input("chose game diffculty: ").lower
    if difficulty == "easy":
        print("You get 10 attempts to guess the number")
        attempts = 10
    elif difficulty == "medium":
        print("You get 6 attempts")
        attempts = 6
    elif difficulty == "hard":
        print("You get 4 attempts")
        attempts = 4
    else:
        print("Invalid difficulty Easy mode selected")
        attempts = 10

    guess = int(input("Enter your guess: "))

    while attempts > 0:
        if guess == random_number:
            print("Congratulations you guessed the correct number!")
            break
        else:
            attempts -= 1
            print(f"Wrong guess. Your guess is too {compare(guess, random_number)}")
            if attempts == 0:
                print(f"You are out of attempts. The number was {random_number}")
            guess = int(input("Enter your guess"))

choice = input("Do you want to play the game").lower()

if choice == "yes":
    play_game()
