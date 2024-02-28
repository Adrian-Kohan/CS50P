from numb3rs import validate

def test_correct_number():
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("257.1.1.1") == False
    assert validate("2.1.1.257") == False
    assert validate("4.257.1.1") == False
    assert validate("4.1.257.1") == False
    assert validate("1.1.1") == False


def test_alphabet():
    assert validate("cs50") == False
