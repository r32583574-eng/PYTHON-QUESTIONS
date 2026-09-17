import random


def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("=== Guess the Number Game ===")
    print("I have chosen a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations!")
            print("You guessed the number in", attempts, "attempts.")
            break


guess_number()
