import math


def maths_operations():
    print("=== Maths Operations ===")

    number = float(input("Enter a number: "))

    print("\nResults:")
    print("Square:", number ** 2)
    print("Square Root:", math.sqrt(number))
    print("Absolute Value:", abs(number))
    print("Ceiling:", math.ceil(number))
    print("Floor:", math.floor(number))


maths_operations()
