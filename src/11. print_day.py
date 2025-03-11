"""
Program to print the day based on the number input.
A program which prompts the user to input day number and computes the corresponding day
if input = 1, output = Monday using modulo 7 for cyclical mapping.
"""

#  Prompt user to input the day number and convert to integer
day_number: int = int(input("Enter the day number: "))

#  Dictionary containing day number with their corresponding day
day_map: dict[int,str] = {
    0:"Sunday",
    1:"Monday",
    2:"Tuesday",
    3:"Wednesday",
    4:"Thursday",
    5:"Friday",
    6:"Saturday"
}

#  Handling negative input
if day_number < 0:
    print(f"Day number {day_number} is not possible.")
else:
    #  Map input to a week cycle using modulo
    day: int = day_number % 7
    print(f"The day for {day_number} is '{day_map[day]}'.")