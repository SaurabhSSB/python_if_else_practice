"""
A program to calculate income tax for the input income by adhering to the Indian rules year 2025.
A program that calculate the income tax on the income and then displays it.

Taxable Income (Rs.)	Tax Rate (%)
0         - 12,00,000	Nil
12,00,001 - 16,00,000	15%
16,00,001 - 20,00,000	20%
20,00,001 - 24,00,000	25%
24,00,000 - above       30%
"""

# Taking the income as input from the user
income: float= float(input("Enter the income:- "))

# Calculating the income tax based on the income given by the user
# Tax slabs: 0-12L (Nil), 12L-16L (15%), 16L-20L (20%), 20L-24L (25%), 24L+ (30%)
if income <= 0:
    # Displaying the income tax on the income which is invalid
    print(f"{income} is not a valid input")
elif income <= 1200000:
    # Displaying the income tax on the income which is Nil
    print(f"Income tax on {income:.2f} is Nil.")
elif income <= 1600000:
    # Displaying the income tax on the income which is 15%
    print(f"Income tax on {income:.2f} is {(income * 15)/100:.2f}")
elif income <= 2000000:
    # Displaying the income tax on the income which is 20%
    print(f"Income tax on {income:.2f} is {(income * 20)/100:.2f}")
elif income <= 2400000:
    # Displaying the income tax on the income which is 25%
    print(f"Income tax on {income:.2f} is {(income * 25)/100:.2f}")
else:
    # Displaying the income tax on the income which is 30%
    print(f"Income tax on {income:.2f} is {(income * 30)/100:.2f}")