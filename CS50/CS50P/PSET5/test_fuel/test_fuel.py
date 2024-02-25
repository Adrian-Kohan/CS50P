from fuel import convert, gauge

def test_correct_input():
    assert convert("1/2") == 50
    assert convert("1/1") == 100

def test_incorrect_input():
    assert convert("100/1") == raise ValueError
    assert convert("a/1") == raise ValueError
    assert convert("100/a") == raise ValueError
    assert convert("a/a") == raise ValueError
    assert convert("1.2") == raise ValueError


def test_zero_y():
    assert convert("100/0") == raise ZeroDivisionError

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
