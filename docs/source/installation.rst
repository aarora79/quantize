Installation
===========

Prerequisites
------------

Before installing the Quantize package, ensure you have the following prerequisites:

- Python 3.8 or higher
- uv (Python package manager) or pip

Installing from Source
---------------------

The recommended way to install Quantize is from source:

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/yourusername/quantize.git
      cd quantize

2. Create a virtual environment using uv:

   .. code-block:: bash

      uv venv

   Alternatively, you can use Python's built-in venv module:

   .. code-block:: bash

      python -m venv .venv

3. Activate the virtual environment:

   - On Windows:

     .. code-block:: bash

        .venv\Scripts\activate

   - On macOS/Linux:

     .. code-block:: bash

        source .venv/bin/activate

4. Install the package in development mode:

   Using uv:

   .. code-block:: bash

      uv pip install -e .

   Using pip:

   .. code-block:: bash

      pip install -e .

Automated Setup
--------------

The repository includes a setup script that automates the installation process:

.. code-block:: bash

   python setup_venv.py

This script will:

1. Create a virtual environment using uv
2. Install the package in development mode
3. Install test dependencies
4. Provide instructions for activating the virtual environment

Dependencies
-----------

Quantize has the following dependencies:

- numpy >= 1.20.0

For development, the following additional packages are recommended:

- pytest >= 7.0.0
- black >= 23.0.0
- isort >= 5.0.0

These development dependencies can be installed with:

.. code-block:: bash

   pip install -e ".[dev]"

Verifying Installation
--------------------

To verify that Quantize is installed correctly, you can run the example script:

.. code-block:: bash

   python example.py

You should see output demonstrating the quantization process with sample values.