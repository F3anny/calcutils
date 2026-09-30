"""calcutils: A simple calculator utilities package."""

import utils.transport
import utils.session
__version__ = "0.1.0"

from .operations import add, multiply, average

__all__ = ["add", "multiply", "average", "__version__"]