"""
Program to check using the sides of a triangle to tell if it is equilateral triangle or not.

Prompt user to input lengths of three side of the triangle and then
evaluate if the triangle is equilateral or not.
"""

side_1: float = float(input("Enter length of side1: "))
side_2: float = float(input("Enter length of side2: "))
side_3: float = float(input("Enter length of side3: "))

if side_1==side_2==side_3:
    print(f"The given triangle is an equilateral triangle.")
else:
    print(f"The given triangle is not an equilateral triangle.")