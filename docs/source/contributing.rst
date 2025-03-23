Contributing
===========

Thank you for your interest in contributing to the Quantize project! This document provides guidelines and instructions for contributing.

Setting Up Development Environment
--------------------------------

1. Fork the repository on GitHub.

2. Clone your fork locally:

   .. code-block:: bash

      git clone https://github.com/yourusername/quantize.git
      cd quantize

3. Set up a development environment:

   .. code-block:: bash

      python setup_venv.py

   This will create a virtual environment and install the package in development mode.

4. Install development dependencies:

   .. code-block:: bash

      pip install -e ".[dev]"

Development Workflow
------------------

1. Create a branch for your changes:

   .. code-block:: bash

      git checkout -b feature/your-feature-name

2. Make your changes to the codebase.

3. Run the tests to ensure your changes don't break existing functionality:

   .. code-block:: bash

      pytest

4. Format your code using Black:

   .. code-block:: bash

      black .

5. Sort imports using isort:

   .. code-block:: bash

      isort .

6. Commit your changes:

   .. code-block:: bash

      git commit -m "Add your meaningful commit message here"

7. Push your changes to your fork:

   .. code-block:: bash

      git push origin feature/your-feature-name

8. Create a pull request from your fork to the main repository.

Code Style
---------

This project follows the Black code style. Please ensure your code is formatted with Black before submitting a pull request.

The project also uses isort to sort imports according to the Black profile.

Testing
------

All new features should include tests. This project uses pytest for testing.

To run the tests:

.. code-block:: bash

   pytest

Documentation
------------

All new features should include documentation. This project uses Sphinx for documentation.

To build the documentation:

1. Install Sphinx and the Read the Docs theme:

   .. code-block:: bash

      pip install sphinx sphinx_rtd_theme

2. Build the documentation:

   .. code-block:: bash

      cd docs
      make html

3. View the documentation by opening ``docs/build/html/index.html`` in your browser.

Pull Request Guidelines
---------------------

1. Include a clear and descriptive title.
2. Include a description of the changes made.
3. Ensure all tests pass.
4. Ensure code is formatted with Black and imports are sorted with isort.
5. Update documentation if necessary.
6. Reference any related issues.

Feature Requests and Bug Reports
------------------------------

If you have a feature request or have found a bug, please open an issue on GitHub.

When reporting a bug, please include:

1. A clear and descriptive title.
2. A description of the expected behavior.
3. A description of the actual behavior.
4. Steps to reproduce the bug.
5. Your environment information (Python version, OS, etc.).

License
------

By contributing to this project, you agree that your contributions will be licensed under the project's MIT license.