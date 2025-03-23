# Quantize

A simple Python library for quantizing floating point values to int4 values.

## Overview

This project demonstrates how to quantize floating point values to int4 values (4-bit integers). Quantization is a technique used to reduce the precision of numbers, which can be useful for:

- Reducing memory usage
- Improving computational efficiency
- Enabling deployment on hardware with limited precision

Int4 quantization specifically reduces floating point values to 4-bit integers, which can only represent 16 distinct values.

## Installation

### Prerequisites

- Python 3.8+
- uv (Python package manager)

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/quantize.git
   cd quantize
   ```

2. Create a virtual environment using uv:
   ```
   uv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source .venv/bin/activate
     ```

4. Install the package in development mode:
   ```
   pip install -e .
   ```

## Usage

```python
from quantize import quantize_to_int4, dequantize_from_int4

# Example floating point values
float_values = [0.1, 0.5, -1.3, 2.7, 3.9, -0.8]

# Quantize to int4
quantized_values, scale, zero_point = quantize_to_int4(float_values)
print(quantized_values)

# Dequantize back to floating point
dequantized_values = dequantize_from_int4(quantized_values, scale)
print(dequantized_values)
```

## Documentation

The full documentation is available at [Read the Docs](https://quantize.readthedocs.io/).

### Building Documentation Locally

To build the documentation locally:

1. Install Sphinx and the Read the Docs theme:
   ```
   pip install sphinx sphinx_rtd_theme
   ```

2. Build the documentation:
   ```
   cd docs
   make html
   ```

3. View the documentation by opening `docs/build/html/index.html` in your browser.

## Contributing

Contributions are welcome! Please see the [Contributing Guide](docs/source/contributing.rst) for more information.

## License

MIT