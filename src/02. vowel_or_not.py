"""
Program to check if a single character is a vowel or not.
The character is taken as input from the user and evaluated based on whether it's a vowel or consonant.
"""

# Taking input fromW user
char: str= input("Enter a single character:- ")

# Checking if the character is vowel or not
if char.lower() in "aeiou":
    # Displaying that the character is a vowel
    print(f"The character '{char}' is vowel.")
else:
    # Displaying that the character is not a vowel
    print(f"The character '{char}' is not a vowel.")