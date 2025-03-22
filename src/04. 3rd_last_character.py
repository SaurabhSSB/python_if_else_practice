"""
Program to check if the 3rd last character of a string is a vowel or not.

The string is taken as input from the user and evaluated based on whether the third last character is vowel or not.
"""

# Taking input from user
char:str= input("Enter a word:- ")

# Check the length of the string
if len(char)<3:
    print(f"The given string {char} is too small.")
else:
    # Checking if the character is vowel or consonant
    if char[-3].lower() in "aeiou":
        # Displaying that the 3rd character is a vowel
        print(f"Third character of {char} from last is a vowel.")
    else:
        # Displaying that the 3rd character is consonant
        print(f"Third character of {char} from last is consonant.")