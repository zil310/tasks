from rational import *


def test_create_normal():
    obj = create(3, 4)
    assert obj.num == 3, 'Error'
    assert obj.den == 4, 'Error'


def test_create_zero_numer():
    obj = create(0, 5)
    assert obj.num == 0, 'Error'
    assert obj.den == 1, 'Error'


def test_create_negative_denominator():
    obj = create(2, -3)
    assert obj.num == -2, 'Error'
    assert obj.den == 3, 'Error'


def test_create_reduction():
    obj = create(6, 8)
    assert obj.num == 3, 'Error'
    assert obj.den == 4, 'Error'


def test_create_denominator_zero():
    try:
        create(1, 0)
        assert False, 'Error'
    except ValueError:
        pass


def test_add_same_denominator():
    a = create(1, 4)
    b = create(2, 4)
    c = add(a, b)
    assert c.num == 3, 'Error'
    assert c.den == 4, 'Error'


def test_add_different_denominators():
    a = create(1, 2)
    b = create(1, 3)
    c = add(a, b)
    assert c.num == 5, 'Error'
    assert c.den == 6, 'Error'


def test_add_negative():
    a = create(1, 2)
    b = create(-1, 4)
    c = add(a, b)
    assert c.num == 1, 'Error'
    assert c.den == 4, 'Error'


def test_add_zero():
    a = create(0, 1)
    b = create(3, 5)
    c = add(a, b)
    assert c.num == 3, 'Error'
    assert c.den == 5, 'Error'


def test_add_result_reduction():
    a = create(1, 2)
    b = create(1, 2)
    c = add(a, b)
    assert c.num == 1, 'Error'
    assert c.den == 1, 'Error'


def test_sub_positive():
    a = create(3, 4)
    b = create(1, 4)
    c = sub(a, b)
    assert c.num == 1, 'Error'
    assert c.den == 2, 'Error'


def test_sub_negative_result():
    a = create(1, 3)
    b = create(1, 2)
    c = sub(a, b)
    assert c.num == -1, 'Error'
    assert c.den == 6, 'Error'


def test_sub_zero():
    a = create(5, 7)
    b = create(0, 1)
    c = sub(a, b)
    assert c.num == 5, 'Error'
    assert c.den == 7, 'Error'


def test_sub_negative_numbers():
    a = create(-1, 2)
    b = create(-1, 4)
    c = sub(a, b)
    assert c.num == -1, 'Error'
    assert c.den == 4, 'Error'


def test_sub_same_denominator_reduction():
    a = create(5, 6)
    b = create(1, 6)
    c = sub(a, b)
    assert c.num == 2, 'Error'
    assert c.den == 3, 'Error'


def test_mul_positive():
    a = create(2, 3)
    b = create(3, 4)
    c = mul(a, b)
    assert c.num == 1, 'Error'
    assert c.den == 2, 'Error'


def test_mul_with_zero():
    a = create(0, 5)
    b = create(7, 2)
    c = mul(a, b)
    assert c.num == 0, 'Error'
    assert c.den == 1, 'Error'


def test_mul_negative():
    a = create(-2, 5)
    b = create(3, 4)
    c = mul(a, b)
    assert c.num == -3, 'Error'
    assert c.den == 10, 'Error'


def test_mul_two_negatives():
    a = create(-1, 2)
    b = create(-2, 3)
    c = mul(a, b)
    assert c.num == 1, 'Error'
    assert c.den == 3, 'Error'


def test_mul_reciprocal():
    a = create(5, 7)
    b = create(7, 5)
    c = mul(a, b)
    assert c.num == 1, 'Error'
    assert c.den == 1, 'Error'


def test_div_normal():
    a = create(1, 2)
    b = create(3, 4)
    c = div(a, b)
    assert c.num == 2, 'Error'
    assert c.den == 3, 'Error'


def test_div_by_one():
    a = create(5, 8)
    b = create(1, 1)
    c = div(a, b)
    assert c.num == 5, 'Error'
    assert c.den == 8, 'Error'


def test_div_negative():
    a = create(2, 3)
    b = create(-4, 5)
    c = div(a, b)
    assert c.num == -5, 'Error'
    assert c.den == 6, 'Error'


def test_div_zero_numerator():
    a = create(0, 1)
    b = create(5, 2)
    c = div(a, b)
    assert c.num == 0, 'Error'
    assert c.den == 1, 'Error'


def test_div_by_zero():
    a = create(3, 4)
    b = create(0, 1)
    try:
        div(a, b)
        assert False, 'Error'
    except ZeroDivisionError:
        pass


def test_power_zero_exponent():
    obj = create(7, 3)
    res = power(obj, 0)
    assert res.num == 1, 'Error'
    assert res.den == 1, 'Error'


def test_power_positive():
    obj = create(2, 3)
    res = power(obj, 3)
    assert res.num == 8, 'Error'
    assert res.den == 27, 'Error'


def test_power_negative_exponent():
    obj = create(2, 3)
    res = power(obj, -2)
    assert res.num == 9, 'Error'
    assert res.den == 4, 'Error'


def test_power_negative_base():
    obj = create(-1, 2)
    res = power(obj, 3)
    assert res.num == -1, 'Error'
    assert res.den == 8, 'Error'


def test_power_large_exponent():
    obj = create(1, 2)
    res = power(obj, 10)
    assert res.num == 1, 'Error'
    assert res.den == 1024, 'Error'


def test_compare_equal():
    a = create(2, 3)
    b = create(4, 6)
    assert compare(a, b) == 0, 'Error'


def test_compare_less():
    a = create(1, 4)
    b = create(1, 2)
    assert compare(a, b) == -1, 'Error'


def test_compare_greater():
    a = create(3, 5)
    b = create(1, 2)
    assert compare(a, b) == 1, 'Error'


def test_compare_with_zero():
    a = create(0, 1)
    b = create(-1, 10)
    assert compare(a, b) == 1, 'Error'


def test_compare_negative():
    a = create(-3, 4)
    b = create(-5, 6)
    assert compare(a, b) == 1, 'Error'


def test_to_int_positive():
    obj = create(7, 3)
    assert to_int(obj) == 2, 'Error'


def test_to_int_negative():
    obj = create(-5, 2)
    assert to_int(obj) == -2, 'Error'


def test_to_int_zero():
    obj = create(0, 5)
    assert to_int(obj) == 0, 'Error'


def test_to_int_exact():
    obj = create(4, 2)
    assert to_int(obj) == 2, 'Error'


def test_to_int_small():
    obj = create(1, 10)
    assert to_int(obj) == 0, 'Error'


def test_to_float_positive():
    obj = create(1, 4)
    assert to_float(obj) == 0.25, 'Error'


def test_to_float_negative():
    obj = create(-3, 2)
    assert to_float(obj) == -1.5, 'Error'


def test_to_float_zero():
    obj = create(0, 100)
    assert to_float(obj) == 0.0, 'Error'


def test_to_float_large():
    obj = create(1000, 3)
    assert abs(to_float(obj) - 333.3333333333333) < 1e-9, 'Error'


def test_to_float_fraction():
    obj = create(22, 7)
    assert abs(to_float(obj) - 3.142857142857143) < 1e-9, 'Error'


def test_to_str_integer_form():
    obj = create(4, 1)
    assert to_str(obj) == "4", 'Error'


def test_to_str_proper_fraction():
    obj = create(3, 5)
    assert to_str(obj) == "3/5", 'Error'


def test_to_str_negative():
    obj = create(-2, 7)
    assert to_str(obj) == "-2/7", 'Error'


def test_to_str_zero():
    obj = create(0, 1)
    assert to_str(obj) == "0", 'Error'


def test_to_str_reduced():
    obj = create(6, 8)
    assert to_str(obj) == "3/4", 'Error'
