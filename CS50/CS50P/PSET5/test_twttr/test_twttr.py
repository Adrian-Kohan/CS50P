form twttr import shorten

def cap():
    assert shorten("HELLO") == "HLL"

def un_cap():
    assert shorten("hello") == "hll"

def without():
    assert shorten("123") == "123"
    