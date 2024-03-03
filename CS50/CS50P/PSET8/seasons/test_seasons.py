from seasons import convert
import sys

def test_incorrect_date_format():
    assert convert("1990.2.2") == sys.exit ("Invalid date")

def test_incorrect_date():
    assert convert("1990.24.50") == sys.exit ("Invalid date")

def test_correct_date():
    if today == "2003-01-01":
        assert convert("2001-01-01") == "One million, fifty-one thousand, two hundred minutes"
