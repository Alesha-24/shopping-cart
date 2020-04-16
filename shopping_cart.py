import pprint
from dotenv import load_dotenv
import os

import operator
from datetime import date
from datetime import time 
from datetime import datetime

load_dotenv() 
tax_rate = os.getenv("tax_rate")

# def timestap():
#     """
#     Formats the receipt timestap in a human friendly format
#     """
#     checkout = datetime.now().strftime("%m/%d/%Y, %r")

def tax_amount_calc(tax_rate, subtotal):
    """
    Calculates the amount of tax to be paid on a purchase 
    Param 1: tax_rate (int/float) enetered as an environment variable
    Param 2: subtotal (int/float) calculated from the product list 
    Example: tax_amount_calc(0.1, 100)
    Returns: 10
    """
    tax_rate = float(tax_rate)
    tax = tax_rate * subtotal
    return tax

def total_calculation(tax,subtotal):
    """
    Calculates the amount of total of a purchase by adding tax to the subtotal  
    Param 1: tax (int/float) calcualted from tax function
    Param 2: subtotal (int/float) calculated from the product list 
    Example: total_calculation(2.50, 40)
    Returns: 42.5
    """
    total = subtotal + float(tax)
    return total 
  
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" 

if __name__ == "__main__":
    
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

    
    checkout = datetime.now().strftime("%m/%d/%Y, %r")

    subtotal = 0
    prod_list = []
    product_selection = []
    shop_name = "The Natural Grocer"

    format("Hello and welcome to " + shop_name + "'s Input System")

    while True: 
        prod_id = input("Please input a product identifier, or 'DONE' if there are no more items: ")
        if prod_id == "DONE":
            print("SHOPPING CART ITEM IDENTIFIERS INCLUDE:", prod_list)
            break      
        else:
            prod_id = int(prod_id)
            matching_products = [p for p in products if p["id"] == prod_id]
            prod_list.append(prod_id)
        try:
            matching_product = matching_products[0]
            print("+ ", matching_product["name"], to_usd(matching_product["price"]))
            product_selection.append(matching_product)
        except IndexError:
            print("The item you entered doesn't exist, please try again")

    receipt = ""
    receipt+="\n------------------------------------------"
    receipt+= "\nThe Natural Grocer"
    receipt+="\n------------------------------------------"
    receipt+= "\nWeb: thenaturalgrocer.com"
    receipt+= "\nPhone: +1 240 360 4848"
    receipt+= "\nCheckout Time:" + checkout
    receipt+="\n------------------------------------------"
    receipt+= "\nShopping Cart Items:"


    for product in product_selection:
        receipt += "\n+ " + str(product["name"]) + " " + str(to_usd(product["price"]))
        price = product["price"]
        subtotal = price + subtotal
        
    receipt+= "\n------------------------------------------"

    tax = tax_amount_calc(tax_rate,subtotal)
    total = total_calculation(tax, subtotal)
    receipt+= f"\nSubtotal: {to_usd(subtotal)}"
    receipt+= f"\nPlus D.C. Sales Tax ({float(tax_rate)*100}%): {to_usd(tax)}"
    receipt+= f"\nTotal: {to_usd(total)}"
    receipt+="\n------------------------------------------"
    receipt+="\nThank you for shopping, please come again!"

    print(receipt)

    #writing receipts to file 
    file_name = os.path.join(os.path.dirname(__file__), "receipts", f"{datetime.now().strftime('%Y-%M-%d-%H-%m-%S')}.txt")
    with open(file_name, 'w') as f:
        f.write(receipt)
