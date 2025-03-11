"""
Program to calculate the count of elements in a string.

A program to prompt a string from user and calculate the number of characters.
"""

str_x: str = input("Enter a string: ")

count: int = 0

for i in str_x:
    count+= 1

print(f"The string {str_x} has {count} characters.")
