"""
Program to display the last digit of a number without indexing.
The number is taken as input from the user and evaluated to display the last digit of the number.
"""

# Taking user input and converting it to integer
num: int= int(input("Enter a number: "))

# Checking if the number is negative
if num<0:
    # Using abs function to ensure that the last digit is positive
    print(f"last digit is {abs(num%10)}")
else:
    # Displaying the last digit using modulo operator
    print(f"last digit is {num%10}")
