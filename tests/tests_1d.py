"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1d.py.
"""
import pytest
from labs.lab_1.lab_1d import two_sum

def test_standard():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1] # Testing standard numbers
    assert two_sum([1, 5, 8, 12, 3], 15) == [3, 4]

def test_negative_nums():
    assert two_sum([-1, -3, 5, 8], 4) == [0, 2] # Testing with negative nums
    assert two_sum([-9, -101, -8, -1], -9) == [2, 3]

def test_invalid_inputs():
    with pytest.raises(ValueError, match = "Invalid list. Please use valid numbers." ): # Testing with invalid list
        two_sum([1, "B", 3], 4)
    with pytest.raises(ValueError, match = "Invalid target. Please use a valid number."): # Testing with invalid target type
        two_sum([2, 7, 11], 9.9)

def test_empty():
    assert two_sum([1, 2, 3], 10) == [] # Testing with no solution
    assert two_sum([], 9) == [] # Testing with empty list