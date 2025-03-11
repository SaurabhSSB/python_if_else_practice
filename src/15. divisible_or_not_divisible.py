"""
Program to check if the 2nd last digit of numerical input from the user is divisible by 3 or not.

Prompts user to input a number and evaluates if the 2nd last digit is divisible by 3 or not.
"""

num: str = input("Enter number: ")

if len(num) > 1:
    if int(num[-2]) % 3 == 0:
        print(f"The last 2nd last digit of number {num} is divisible by 3.")
    else:
        print(f"The last 2nd last digit of number {num} is not divisible by 3.")
else:
    print("2nd digit does not exist.")