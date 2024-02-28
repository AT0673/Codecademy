# else statements allow us to elegantly describe what we want our code to do when certain conditions are not met.
# else statements always appear in conjunction with if statements.

credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
# If a student is failing to meet one or both graduation requirements, they want it to print:
#   "You do not meet the requirements to graduate."
#Add an else statement to the existing if statement.
else:
  print("You do not meet the requirements to graduate.")