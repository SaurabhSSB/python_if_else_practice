"""
Program to check if the first and last number of a list is same or not.
Compare the first and last number of a pre-defined list and print same if same otherwise different.
"""

# List
l1: list= [11, 15, 14, 27, 39]

# Checking if the first and last number of list are same or different
if l1[0] == l1[-1]:
    # Displaying that the first and last number of list are same
    print("The first and last number of the list are same.")
else:
    # Displaying that the first and last number of list are different
    print("The first and last number of the list are different.")