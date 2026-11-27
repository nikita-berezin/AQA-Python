def calculate_price(base, discount):
    return base - discount

def test_price_calculation():
    assert calculate_price(100, 10) == 90