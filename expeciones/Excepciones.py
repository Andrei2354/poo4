import pytest

def divide(a, b):
    if(b  == 0):
        raise ValueError("Cannot divide by zero")

def test_exception():
    a = 0
    b = 10
    with pytest.raises(ZeroDivisionError):
        b / a 


def test_divide():
    with pytest.raises(ZeroDivisionError) as exeption_info:
        divide(10,0)
    assert str(exeption_info.value).lower == "Cannot divide by zero"


