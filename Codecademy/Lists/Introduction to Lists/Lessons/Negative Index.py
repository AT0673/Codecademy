#What if we want to select the last element of a list?
#We can use the index -1 to select the last item of a list, even when we don’t know how many elements are in a list.

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]
last_element = shopping_list[-1]   #<---- This selects the last element within a list.
index5_element = shopping_list[5]  #<---- This also selects the last element within a list, as the 5th element is the last.
print(last_element)
print(index5_element)