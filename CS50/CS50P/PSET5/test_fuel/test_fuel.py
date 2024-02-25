from fuel import convert, gauge
import pytest

def test_correct_input():
    assert convert("1/2") == 50
    assert convert("1/1") == 100

def test_incorrect_input():
    with pytest.raises(ValueError):
        convert("x/y")
        

def test_zero_y():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
