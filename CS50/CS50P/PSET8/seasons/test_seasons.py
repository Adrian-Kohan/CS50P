from seasons import convert
from datetime import date
import sys

def test_incorrect_date_format():
    assert convert("1990.2.2", date(2003, 1, 1)) == sys.exit ("Invalid date")

def test_incorrect_date():
    assert convert("1990.24.50", date(2003, 1, 1)) == sys.exit ("Invalid date")

def test_correct_date():
    assert convert(date(2001, 1, 1), date(2003, 1, 1)) == "One million, fifty-one thousand, two hundred minutes"
