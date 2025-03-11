"""
A Program to check whether a string starts with vowel or not.
This program will traverse the first character of string and evaluate whether the character is vowel or consonant.
"""

# Taking string as input from the user
variable: str= input("Enter the string:- ")

# Checking if the first character is vowel or consonant
if variable[0].lower() in "aeiou":
    # Displaying that the string starts with vowel
    print(f"The given string '{variable}' starts with a vowel.")
else:
    # Displaying that the string starts with consonant
    print(f"The given string '{variable}' starts with a consonant.")