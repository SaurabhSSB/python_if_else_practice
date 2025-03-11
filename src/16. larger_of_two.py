"""
Python program that takes two numbers as input from the user and prints the larger of the two numbers.

Prompts the user to input two numbers and displays the larger number.
"""

num_1: int = int(input("Enter number 1: "))
num_2: int = int(input("Enter number 2: "))

if num_1 > num_2:
    print(f"{num_1} is larger of the two.")
elif num_1 < num_2:
    print(f"{num_2} is larger of the two.")
else:
    print("Both numbers are equal.")