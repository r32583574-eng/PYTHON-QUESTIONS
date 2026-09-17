import random


def generate_otp():
    otp = random.randint(100000, 999999)

    print("=== OTP Generator ===")
    print("Your OTP is:", otp)


generate_otp()
