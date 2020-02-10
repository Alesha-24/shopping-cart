import pprint

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#error message for products not in the list 
#print(products)
import operator
from datetime import date
from datetime import time 
from datetime import datetime

def to_usd(my_price):
    return f"${my_price:,.2f}" 

print("-----------------------------------------------")
print("Hello and welcome to The Natural Grocer's Input System")
print("-----------------------------------------------")

subtotal = 0
prod_list = []
product_selection = []

while True: 
    prod_id = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    if prod_id == "DONE":
        print("SHOPPING CART ITEM IDENTIFIERS INCLUDE:", prod_list)
        break 
    else:
        prod_id = int(prod_id)
        matching_products = [p for p in products if p["id"] == prod_id]
    try:
        matching_product = matching_products[0]
        print("+ ", matching_product["name"], to_usd(matching_product["price"]))
        product_selection.append(matching_product)
    except IndexError:
        print("The item you entered doesn't exist, please try again")

print(product_selection)


print("------------------------------------------")
print("The Natural Grocer")
print("------------------------------------------")
print("Web: thenaturalgrocer.com")
print("Phone: +1 240 360 4848")
today = datetime.now()
print("Checkout Time:", today.year, "/", today.month, "/", today.day, "  ", today.hour, ":", today.minute)
print("------------------------------------------")
print("Shopping Cart Items:")


for product in product_selection:
    print("+ ", product["name"], to_usd(product["price"]))
    price = product["price"]
    subtotal = price + subtotal
print("------------------------------------------")

print(to_usd(subtotal))
tax = 0.0875
amount_tax = tax * subtotal
print("Plus D.C. Sales Tax (8.75%): ", to_usd(amount_tax))
total = subtotal + amount_tax 
print(to_usd(total)) 
print("------------------------------------------")
print("Thank you for shopping, please come again!")
