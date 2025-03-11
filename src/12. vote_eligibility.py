"""
Program to check whether a person is eligible to vote or not based on their age.

A program which prompts the user to enter age and
determines if the person is allowed to vote (age 18 or older) or not.
"""
age: int = int(input("Enter age: "))

if age >= 18:
    print("Person eligible to vote.")
else:
    print("Person not eligible to vote.")