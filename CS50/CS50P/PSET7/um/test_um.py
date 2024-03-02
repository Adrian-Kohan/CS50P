from um import count

def test_only_um():
    assert count("um ") == 1
    assert count("hi") == 0

def test_um_in_middle():
    assert count("yummy") == 0

def test_multiple_um():
    assert count("Um, thanks, um...") == 2