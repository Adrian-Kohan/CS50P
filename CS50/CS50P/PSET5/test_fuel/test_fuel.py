from fuel import convert

def test_only_numbers():
    assert convert("1/2") == "50%"
    assert convert("1/1") == "F"
    assert convert("1/100") == "E"


def test_
