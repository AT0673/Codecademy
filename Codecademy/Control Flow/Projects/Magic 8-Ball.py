# Task 1. Declare a name variable.
# Task 2. Declare a question variable. 
# Task 3. Store the answer as an empty string.
# Task 4. Generate a random number.
# Task 5. Create a variable to store the random number.
# Task 6. If statement where if random_number == 1, answer = “Yes - definitelY”
# Task 7. elif statement after where if; random_number == 2, answer == “It is decidedly so”. Then, continue  for each of the remaining phrases for the values 3 to 9. 
# Task 8. After if/elif statements, add an else statement that will set answer == “Error”, if the number was accidentally assigned a value outside of our range.
# Task 9. Write a print() statement to output the asker’s name and their question, which should be in the following format: [Name] asks: [Question]
# Task 10. Add a second print() statement that will output the Magic 8-Ball’s answer in the following format: Magic 8-Ball's answer: [answer]
# Optional Task. What if the asker does not provide a name, such that the value of name is an empty string? If the name string is empty, the output of the program looks like the following:

import random

name = "Alfie"
question = "Will it rain tomorrow"
answer = ""
random_number = random.randint(1, 9)                #Generates a number between 1 and 9. 

if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
else:
    answer = "Error"

if question == "":
    print("The Magic 8-Ball cannot predict silence. ")
else:
    if name == "":
        print("Question: ", question)
        print("Magic 8 Ball's Answer: ", answer)
    else:
        print(name, "asks: ", question)
        print("Magic 8 Ball's Answer: ", answer)

