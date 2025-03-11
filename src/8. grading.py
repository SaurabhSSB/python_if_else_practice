"""
A program to calculate percentage of a student through 5 subjects. Take marks as input from the user.
Using percentage print which grade the student has scored.

A program that will ask for marks of five subjects and maximum possible marks.
Then the total percentage will be calculated, after that grading will be done.
100- 91 - A+
90 - 81 - A
80 - 71 - B+
70 - 61 - B
60 - 51 - C+
50 - 41 - C
40 - 31 - D
30 - 00 - Fail
"""

# Initializing total_earned_marks variable for keeping track of total marks scored
total_earned_marks: float= 0
# Initializing total_possible_marks variable for keeping track of total possible marks
total_possible_marks: int= 0

# Taking marks of five subject along with maximum marks as input and converting it to integer using for loop
for i in range(1,6):
    y=int(input(f"Enter marks of Subject {i}:- "))
    z=int(input(f"Enter maximum marks of Subject {i}:- "))
    # Updating the value of the marks earned and maximum marks
    total_earned_marks+= y
    total_possible_marks+= z

# Checking that the total_earned_marks is less than or equal to total_possible marks
if total_earned_marks <= total_possible_marks:
    # percentage_5_subject for calculating percentage of the 5 subjects together
    percentage_5_subject: float= (total_earned_marks/total_possible_marks) *100
    print(f"Total Percentage is {percentage_5_subject: .2f}.")
    if percentage_5_subject >= 91:
        print("The grade of the student is A+.")
    elif percentage_5_subject >= 81:
        print("The grade of the student is A.")
    elif percentage_5_subject >= 71:
        print("The grade of the student is B+.")
    elif percentage_5_subject >= 61:
        print("The grade of the student is B.")
    elif percentage_5_subject >= 51:
        print("The grade of the student is C+.")
    elif percentage_5_subject >= 41:
        print("The grade of the student is C.")
    elif percentage_5_subject >= 31:
        print("The grade fo the student is D.")
    else:
        print("The status of student is fail.")
else:
    print("Not Possible")