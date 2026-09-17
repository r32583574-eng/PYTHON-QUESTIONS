import math
import random


def calculator():
    print("\n=== Calculator ===")

    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator.")
        return

    print("Result:", result)


def fibonacci():
    print("\n=== Fibonacci Series ===")

    n = int(input("Enter the number of terms: "))

    first = 0
    second = 1

    print("Fibonacci Series:")

    for _ in range(n):
        print(first, end=" ")
        first, second = second, first + second

    print()


def prime_number():
    print("\n=== Prime Number Checker ===")

    number = int(input("Enter a number: "))

    if number <= 1:
        print(number, "is not a prime number.")
        return

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(number, "is not a prime number.")
            return

    print(number, "is a prime number.")


def guess_number():
    print("\n=== Guess the Number Game ===")
    print("Guess a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0

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


def generate_otp():
    print("\n=== OTP Generator ===")

    otp = random.randint(100000, 999999)

    print("Your OTP is:", otp)


def bill_generator():
    print("\n=== Bill Generator ===")

    item = input("Enter item name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    total = price * quantity

    print("\n----- BILL -----")
    print("Item:", item)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total:", total)
    print("----------------")


def student_information():
    print("\n=== Student Information ===")

    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter course name: ")
    college = input("Enter college name: ")

    print("\n----- STUDENT DETAILS -----")
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
    print("College:", college)
    print("---------------------------")


def maths_operations():
    print("\n=== Maths Operations ===")

    number = float(input("Enter a number: "))

    print("\nResults:")
    print("Square:", number ** 2)

    if number >= 0:
        print("Square Root:", math.sqrt(number))
    else:
        print("Square Root: Not available for negative numbers")

    print("Absolute Value:", abs(number))
    print("Ceiling:", math.ceil(number))
    print("Floor:", math.floor(number))


def main():
    while True:
        print("\n================================")
        print("       MY PYTHON PROJECT")
        print("================================")
        print("1. Calculator")
        print("2. Fibonacci Series")
        print("3. Prime Number Checker")
        print("4. Guess the Number")
        print("5. OTP Generator")
        print("6. Bill Generator")
        print("7. Student Information")
        print("8. Maths Operations")
        print("9. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            calculator()
        elif choice == "2":
            fibonacci()
        elif choice == "3":
            prime_number()
        elif choice == "4":
            guess_number()
        elif choice == "5":
            generate_otp()
        elif choice == "6":
            bill_generator()
        elif choice == "7":
            student_information()
        elif choice == "8":
            maths_operations()
        elif choice == "9":
            print("Thank you for using My Python Project!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
