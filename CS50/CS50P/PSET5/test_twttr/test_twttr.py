from twttr import shorten

def test_cap_vowel():
    assert shorten("HELLO") == "HLL"

def test_un_cap_vowel():
    assert shorten("hello") == "hll"

def test_without_vowel():
    assert shorten("123") == "123"
