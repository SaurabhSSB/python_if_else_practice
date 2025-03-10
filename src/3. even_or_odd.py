"""
Program to check if a number is even or odd where the number is taken as input.
The number is taken as input from the user and then evaluated based on divisibility by 2.
"""


# Taking input from user and converting it to integer
num: int= int(input("Enter the number: "))

# Checking if the number is odd or even
if num%2== 0:
    # Displaying that the number is even
    print(f"{num} is an even number.")
else:
    # Displaying that the number is odd
    print(f"{num} is odd number.")