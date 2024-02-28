#   class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]
#"Jenny" changed their mind and is now more interested in "Meditation". 
#We will need to modify the list to accommodate the change to our class_name_hobbies list. To change a value in a two-dimensional list, reassign the value using the specific index.
# The list of Jenny is at index 0. The hobby is at index 1. 
#       class_name_hobbies[0][1] = "Meditation"
#       print(class_name_hobbies) 


incoming_class = [["Kenny", "American", 9], ["Tanya", "Ukrainian", 9], ["Madison", "Indian", 7]]
print(incoming_class )

incoming_class[2][2] = 8   #<---- This will change Madison's, at index 2, grade, at index 2.
print(incoming_class)

incoming_class[-3][-3] = "Ken"   #<--- This does the same, just in negative indices, thus counting backwards. 
print(incoming_class)