# calcutils-fanny

A simple calculator utilities package providing basic mathematical operations with type hints and comprehensive documentation.

## Features

- **add(a, b)**: Add two numbers together
- **multiply(a, b)**: Multiply two numbers together  
- **average(numbers)**: Calculate the arithmetic mean of a list of numbers

## Installation

Install from PyPI (once published):

```bash
pip install calcutils-fanny
```

Or install from source:

```bash
git clone https://github.com/Fanny/calcutils.git
cd calcutils
pip install .
```

## Usage

```python
from calcutils import add, multiply, average

# Basic arithmetic
result = add(2.5, 3.7)  # 6.2
product = multiply(4, 5)  # 20.0

# Calculate average
numbers = [1, 2, 3, 4, 5]
avg = average(numbers)  # 3.0

# Handle empty lists gracefully
empty_avg = average([])  # 0.0
```

## Development

To set up for development:

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Unix)
4. Install development dependencies: `pip install -r requirements-dev.txt`
5. Run tests: `pytest`

## Building

To build the package:

```bash
python -m build
```

This creates both source distribution (`.tar.gz`) and wheel (`.whl`) files in the `dist/` directory.

## License

MIT License - see LICENSE file for details.

## Author

Fanny Iribagiza (iribagizafanny3@gmail.com)