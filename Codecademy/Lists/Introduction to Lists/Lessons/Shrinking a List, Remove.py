# We can remove elements in a list using the .remove() Python method. 

order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list)

order_list.remove("Flatbread")  #<---- This removes the element 'flatbread' from our list.
print(order_list)


new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)
new_store_order_list.remove("Mango")   #<--- This removes the duplicate 'Mango' element from our list 
print(new_store_order_list)

new_store_order_list.remove("Onions")    #<---- This will not work, as we do not have an "Onions" element within our list.