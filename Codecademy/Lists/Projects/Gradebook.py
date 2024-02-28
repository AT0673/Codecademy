last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]


subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])         #Adds 2 new subjects and scores into the 2D list.
print(gradebook)

gradebook[-1][-1] = 98   #Sets the visual arts score to 98. [-1] selects visual arts, [-1] selects scores.
print(gradebook)

gradebook[2].remove(85) #Selects the 3rd list, and removes the score of '85'


gradebook[2].append("Pass")   #This selects the 2nd list and adds a new score, 'Pass' to it.

full_gradebook = last_semester_gradebook + gradebook
print("Full gradebook is: ", full_gradebook)
