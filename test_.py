import pytest
import myfactorial

def test_myfactorial():
    assert myfactorial.factorial(10) == 3628800
