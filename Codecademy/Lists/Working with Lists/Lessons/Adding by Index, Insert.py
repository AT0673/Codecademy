#The Python list method .insert() allows us to add an element to a specific index in a list.
#The .insert() method takes in two inputs:
    #The index you want to insert into.
    #The element you want to insert at the specified index.

front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below: 

front_display_list.insert(0, "Pineapple")    # This selects the first element of the list, and adds Pineapple instead, moving the previous 0th element; Mango, to element 1.
print(front_display_list)