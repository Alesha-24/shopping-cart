import pytest 

from app.shopping_cart import subtotal_calc, to_usd, find_product, tax_amount_calc, total_calculation

def test_to_usd(): 
    # it should apply USD formatting
    assert to_usd(2.40) == "$2.40"

    # it should display two decimal places
    assert to_usd(2.4) == "$2.40"

    # it should round to two places
    assert to_usd(2.4000003) == "$2.40"

    # it should display thousands separators
    assert to_usd(1234567890.5555555) == "$1,234,567,890.56"

def test_find_product():
    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    ]

    # if there is a match, it should find and return a product
    matching_product = find_product("2", products)
    assert matching_product["name"] == "All-Seasons Salt"

    # if there is no match, it should raise an IndexError
    with pytest.raises(IndexError):
        find_product("2222", products)

def test_subtotal_calc():
    # verifies that the subtotal is calculated by adding the price of all products in a list 
    selected_products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99}]
    assert subtotal_calc(selected_products) == 10.98

def test_total_calculation():
    # checks that the total is correctly cacluating the sum of the tax amount and subtotal
    assert total_calculation(2, 12) == 14
    
def test_tax_amount_calc():
    # checks that the tax amount is calculated as the tax rate multiplied by the subtotal 
    assert tax_amount_calc(0.06, 24) == 1.44