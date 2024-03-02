from working import convert

def test_correct_input_time:
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_incorrect_input_time:
    with pytest.raises(ValueError):
        assert convert("09:00 AM - 17:00 PM")
        assert convert("9 AM - 5 PM")


def test_incorrect_time:
    with pytest.raises(ValueError):
        assert convert("9:60 AM to 5:60 PM")