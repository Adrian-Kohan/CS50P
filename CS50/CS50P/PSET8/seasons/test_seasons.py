from seasons import convert
from datetime import date
import pytest

def test_incorrect_date_format():
    with pytest.raises(SystemExit):
        assert convert("1990.2.2", date(2003, 1, 1))

def test_incorrect_date():
    with pytest.raises(SystemExit):
        assert convert("1990.24.50", date(2003, 1, 1)) == "Invalid date"

def test_correct_date():
    assert convert("2001-1-1", date(2003, 1, 1)) == "One million, fifty-one thousand, two hundred minutes"
