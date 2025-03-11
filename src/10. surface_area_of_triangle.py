"""
Program to calculate the surface area of a triangle.
Prompts the user for the lengths of the three sides and computes the surface area of triangle using:
√[s(s-a)(s-b)(s-c)]
s is semi-perimeter (a+b+c)/2.
a,b,c are the side lengths.
"""

# Prompt user for three side lengths of triangle and convert to float
side_1: float = float(input("Enter first side length of triangle: "))
side_2: float = float(input("Enter second side length triangle: "))
side_3: float = float(input("Enter third side length of triangle: "))

# Checking whether the application of Heron's formula is possible
if side_1 <= 0 or side_2 <= 0 or side_3 <= 0:
    print("Side lengths must be positive.")
elif (side_1 + side_2 <= side_3) or (side_2 + side_3 <= side_1) or (side_1 + side_3 <= side_2):
    print("These side lengths cannot form a triangle.")
else:
    # Calculating semi_perimeter
    semi_perimeter: float = (side_1+side_2+side_3)/2
    # Apply Surface Area formula √[s(s-a)(s-b)(s-c)]
    surface_area= (semi_perimeter * (semi_perimeter - side_1) * (semi_perimeter - side_2) * (semi_perimeter - side_3)) ** 1/2
    # Displaying Surface Area of the triangle
    print(f"Surface area of the triangle is {surface_area:.2f}.")