import pytest

from src.power_calculator import square_number, cube_number, fifth_power_of_number

def test_square_number():
    assert square_number(2) == 4, "Test Failed: Square of 2 should be 4"
    assert square_number(3) == 9, "Test Failed: Square of 3 should be 9"

def test_cube_number():
    assert cube_number(2) == 8, "Test Failed: Cube of 2 should be 8"
    assert cube_number(3) == 27, "Test Failed: Cube of 3 should be 27"


def test_fifth_power_of_number():
    assert fifth_power_of_number(2) == 32, "Test Failed: Fifth power of 2 should be 32"
    assert fifth_power_of_number(3) == 243, "Test Failed: Fifth power of 3 should be 243"

def test_invalid_input():
    with pytest.raises(TypeError):
        square_number("string")