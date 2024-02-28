# You can build larger boolean expressions using boolean operators. These operators (also known as logical operators) combine smaller boolean expressions into larger boolean expressions.
# The three operators are; and, or, not.

# 'and' combines two boolean expressions and evaluates as True if both its components are True, but False otherwise.

statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

credits = 120
gpa = 3.4

# Students now also need a 2.0 or higher GPA. Rewrite the if statement so that it checks to see if a student meets both requirements using an and statement. 
if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")