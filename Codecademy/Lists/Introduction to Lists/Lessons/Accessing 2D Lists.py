# heights = [["Noelle", 61], ["Ali", 70], ["Sam", 67]].
# If we wanted to access "Noelle"‘s height: 
# Access the sublist at index 0, and then access the 1st index of that sublist. 
# noelles_height = heights[0][1]    <---- The [0] signifies that we are picking the first list, and then the [1] 1st element within that 1st list.

class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
print(class_name_test)

# Select Sam's test score.
sams_score = class_name_test[2][1]    #<---- This selects the 3rd list, and then the 2nd element within that list.
print(sams_score)

ellies_score = class_name_test[-1][-1]    #<---- This does the same, it selects the last list as [-1] specifies the last, and then the last element within the last list. 
print(ellies_score)