form twttr import shorten

def cap_vowel():
    assert shorten("HELLO") == "HLL"

def un_cap_vowel():
    assert shorten("hello") == "hll"

def without_vowel():
    assert shorten("123") == "123"
