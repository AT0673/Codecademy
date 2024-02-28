# This operator is straightforward: when applied to any boolean expression it reverses the boolean value. So if we have a True statement and apply a not operator we get a False statement.

statement_one = not (4 + 5 <= 9)

statement_two = not (8 * 2) != 20 - 4

credits = 120
gpa = 1.8

# Return to a previous if statement and add in several checks using and and not statements: If a student’s credits is not greater or equal to 120, If their gpa is not greater or equal to 2.0, If their credits is not greater than or equal to 120 and their gpa is not greater than or equal to 2.0.

if not credits >= 120:
    print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
    print("Your GPA is not high enough to graduate.")

if not credits >= 120 and not gpa >= 2.0:
    print("You do not meet either requirement to graduate!")