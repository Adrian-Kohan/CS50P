from plates import is_valid

def test_start_with_letter():
    assert is_valid("cs50") == True
    assert is_valid("222aA") == False

def test_lenght():
    assert is_valid("cs50") == True
    assert is_valid("cssffladf50") == False
    assert is_valid("H") == False


def test_number():
    assert is_valid("cs50") == True
    assert is_valid("cs50p") == False
    assert is_valid("cs050") == False
    assert is_valid("50cs") == False



def test_punctuation_marks():
    assert is_valid("cs50") == True
    assert is_valid("cs/.50") == False

def test_spaces():
    assert is_valid("cs50") == True
    assert is_valid("cs 50") == False
