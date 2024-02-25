from twttr import shorten

def test_cap_vowel():
    assert shorten("HELLO, THERE") == "HLL, THR"

def test_un_cap_vowel():
    assert shorten("hello, there") == "hll, thr"

def test_without_vowel():
    assert shorten("123") == "123"
