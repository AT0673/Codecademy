#When we want to add multiple items to a list, we can use + to combine two lists (this is also known as concatenation).


orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:

new_orders = ["lilac", "iris"]
orders_combined = orders + new_orders


broken_prices = [5, 3, 4, 5, 4] + [4] #<---- This cannot be just a regular 4 as you cannot add integers to lists. It has to be within the [] to be added.