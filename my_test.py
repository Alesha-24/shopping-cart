import pytest 

from shopping_cart import to_usd, tax_amount_calc, total_calculation

def test_to_usd(): 
    # it should apply USD formatting
    assert to_usd(2.40) == "$2.40"

    # it should display two decimal places
    assert to_usd(2.4) == "$2.40"

    # it should round to two places
    assert to_usd(2.4000003) == "$2.40"

    # it should display thousands separators
    assert to_usd(1234567890.5555555) == "$1,234,567,890.56"

def test_total_calculation():
    assert total_calculation(4, 12) == 16
    
def test_tax_amount_calc():
    assert tax_amount_calc(0.06, 24) == 1.44