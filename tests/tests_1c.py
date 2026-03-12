"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_standard():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6

def test_all_negative():
    assert max_subarray_sum([-5, -1, -8]) == -1

def test_single_element():
    assert max_subarray_sum([5]) == 5

def test_empty():
    assert max_subarray_sum([]) == 0

def test_invalid():
    with pytest.raises(ValueError, match = "Invalid input. Please enter a list of valid numbers."):
        max_subarray_sum([1, "a", 3])
    with pytest.raises(ValueError, match = "Invalid input. Please enter a list of valid numbers."):
        max_subarray_sum(["@", 5, 2])