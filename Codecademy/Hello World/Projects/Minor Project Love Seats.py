# This project is designed as 'building a system to help speed up the process of creating receipts for  customers.
# In this project, I will be storing the names and prices of a furniture store’s catalog in variables. Then process the total price and item list of customers, printing them to the output terminal.


# Adding a description for one of the 'Love Seats'.
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""

# Creating a float for the cheapest love seat.
lovely_loveseat_price = 254.00

# Adding a description for another 'Love Seat'
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
# Adding the price for the newest seat. 
stylish_settee_price = 180.50

# Adding another product description.
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
# Adding the price for the new product. 
luxurious_lamp_price = 52.15

# Adding sales tax to the inevitable receipt. 
sales_tax = 0.088

# Variable for the total of 'Customer One's' purchases.
customer_one_total = 0 

#Variable for the descriptions of the items 'Customer One' is purchasing.
customer_one_itemization = ""

# Adding the newest purchase (The Loveseat) price to the total spent.
customer_one_total += 254.00

# Adding the description of the item the customer bought to the itemization variable.
customer_one_itemization += lovely_loveseat_description

# The customer has decided to purchase the Luxurious Lamp! Let’s add the price to the customer’s total.
customer_one_total += 52.15

#Let’s keep the itemization up-to-date and add the description of the Luxurious Lamp to our itemization.
customer_one_itemization += luxurious_lamp_description

#They’re ready to check out! Let’s begin by calculating sales tax.
customer_one_tax = customer_one_total * sales_tax

# Adding the sales tax.
customer_one_total += customer_one_tax

#Let’s start printing up their receipt!
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total: ")
print(customer_one_total)