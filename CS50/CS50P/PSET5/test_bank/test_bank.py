from bank import value

def test_with_hello():
    assert value("hello, there") == "$0"
    assert value("Hello, there") == "$0"

def test_with_h_at_first():
    assert value("hi, there") == "$20"
    assert value("Hi, there") == "$20"

def test_without_h():
    assert value("WHAT'S UP") == "$100"
    assert value("what's up") == "$100"
    assert value("123") == "$100"




