"""Tests for calcutils operations module."""

import pytest
from calcutils.operations import add, multiply, average


class TestAdd:
    """Test cases for the add function."""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        assert add(2, 3) == 5
        assert add(1.5, 2.5) == 4.0
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add(-2, -3) == -5
        assert add(-1.5, -2.5) == -4.0
    
    def test_add_mixed_signs(self):
        """Test adding numbers with different signs."""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2
    
    def test_add_with_zero(self):
        """Test adding with zero."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0


class TestMultiply:
    """Test cases for the multiply function."""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert multiply(2, 3) == 6
        assert multiply(2.5, 4) == 10.0
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert multiply(-2, -3) == 6
        assert multiply(-2.5, -4) == 10.0
    
    def test_multiply_mixed_signs(self):
        """Test multiplying numbers with different signs."""
        assert multiply(2, -3) == -6
        assert multiply(-2, 3) == -6
    
    def test_multiply_with_zero(self):
        """Test multiplying with zero."""
        assert multiply(0, 5) == 0
        assert multiply(5, 0) == 0
        assert multiply(0, 0) == 0
    
    def test_multiply_with_one(self):
        """Test multiplying with one."""
        assert multiply(1, 5) == 5
        assert multiply(5, 1) == 5


class TestAverage:
    """Test cases for the average function."""
    
    def test_average_positive_numbers(self):
        """Test averaging positive numbers."""
        assert average([1, 2, 3, 4, 5]) == 3.0
        assert average([2, 4, 6]) == 4.0
    
    def test_average_negative_numbers(self):
        """Test averaging negative numbers."""
        assert average([-1, -2, -3]) == -2.0
    
    def test_average_mixed_signs(self):
        """Test averaging numbers with different signs."""
        assert average([-2, 2]) == 0.0
        assert average([-1, 1, 2]) == 2/3
    
    def test_average_single_number(self):
        """Test averaging a single number."""
        assert average([5]) == 5.0
        assert average([0]) == 0.0
    
    def test_average_empty_list(self):
        """Test averaging an empty list (edge case)."""
        assert average([]) == 0.0
    
    def test_average_floats(self):
        """Test averaging floating point numbers."""
        assert average([1.5, 2.5, 3.0]) == 7.0/3
        assert pytest.approx(average([0.1, 0.2, 0.3])) == 0.2