from food_order import food_order


def test_order1():
    assert food_order(10, 2) == 20

def test_order2():
    assert food_order(10, 3) == 30

def test_order3():
    assert food_order(20, 5) == 100


def test_order4():
    assert food_order(5, 2) == 10

def test_order5():
    assert food_order("abc", 2) == "invalid price"

def test_order6():
    assert food_order(10, "two") == "invalid quantity"