# In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

weight = 8.4

# Ground Shipping.
if weight <= 2:
    cost_ground = weight * 1.5 + 20
    print(cost_ground)
elif weight >= 3 or weight <= 6:
    cost_ground = weight * 3 + 20
    print(cost_ground)
elif weight >= 7 or weight == 10:
    cost_ground = weight * 4 + 20
    print(cost_ground)
else:
    cost_ground = weight * 4.75 + 20
    print(price)