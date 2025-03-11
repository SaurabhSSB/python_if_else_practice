"""
A program to convert a Celsius value to Fahrenheit
The program will take Celsius value as input and convert the value to Fahrenheit and
displays the result rounded to two decimal places.
F= (C * 9/5) + 32
"""

# Prompt user for Celsius temperature and convert to float
celsius: float= float(input("Enter the temperature in celsius: "))

# Apply conversion formula: F = (C * 9/5) + 32
fahrenheit: float= (celsius * 9/5) + 32

# Display result with two decimal places
print(f"The value of temperature in fahrenheit is {fahrenheit: .2f}.")