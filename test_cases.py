def apply_discount(price, percent):
    return price - (price * percent / 100)


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b





def test_normal_discount():
    result = apply_discount(100,20)
    assert result == 80

def test_zero_discount():
    result = apply_discount(100, 0)
    assert result == 100

def test_edge_case_discount():
    result = apply_discount(100, 100)
    assert result == 0

def test_normal_division():
    result = divide(10,2)
    assert result == 5

def test_decimal_results():
    result = divide(5, 2)
    assert result == 2.5

def test_division_by_zero():
    try:
        result = divide(10, 0)
        assert False
    
    except ValueError:
        assert True




test_normal_discount()
test_zero_discount()
test_edge_case_discount()

test_normal_division()
test_decimal_results()
test_division_by_zero()
print('All test cases passed!')