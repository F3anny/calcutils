"""Mathematical operations for the calcutils package."""

from typing import List


def add(a: float, b: float) -> float:
    """Add two numbers together.
    
    Args:
        a: First number to add
        b: Second number to add
        
    Returns:
        The sum of a and b
        
    Examples:
        >>> add(2.5, 3.7)
        6.2
        >>> add(-1, 1)
        0.0
    """
    return a + b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers together.
    
    Args:
        a: First number to multiply
        b: Second number to multiply
        
    Returns:
        The product of a and b
        
    Examples:
        >>> multiply(3, 4)
        12.0
        >>> multiply(2.5, 2)
        5.0
    """
    return a * b


def average(numbers: List[float]) -> float:
    """Calculate the average of a list of numbers.
    
    Args:
        numbers: List of numbers to average
        
    Returns:
        The arithmetic mean of the numbers, or 0.0 if the list is empty
        
    Examples:
        >>> average([1, 2, 3, 4, 5])
        3.0
        >>> average([])
        0.0
        >>> average([2.5, 7.5])
        5.0
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)