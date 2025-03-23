#!/usr/bin/env python3
"""
Script to set up a virtual environment using uv and install the package.
"""

import os
import platform
import subprocess
import sys


def run_command(command, cwd=None):
    """Run a command and print its output."""
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
    
    if result.stdout:
        print(result.stdout)
    
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    
    if result.returncode != 0:
        print(f"Command failed with exit code {result.returncode}")
        sys.exit(result.returncode)
    
    return result


def main():
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create virtual environment using uv
    print("\n=== Creating virtual environment using uv ===")
    run_command(["uv", "venv"], cwd=script_dir)
    
    # Install the package in development mode using uv
    print("\n=== Installing package in development mode ===")
    run_command(["uv", "pip", "install", "-e", "."], cwd=script_dir)
    
    # Install test dependencies using uv
    print("\n=== Installing test dependencies ===")
    run_command(["uv", "pip", "install", "pytest"], cwd=script_dir)
    
    # Print activation instructions
    print("\n=== Virtual environment setup complete ===")
    print("To activate the virtual environment:")
    
    if platform.system() == "Windows":
        print("    .venv\\Scripts\\activate")
    else:
        print("    source .venv/bin/activate")
    
    print("\nTo run the example:")
    print("    python example.py")
    
    print("\nTo run the tests:")
    print("    pytest")


if __name__ == "__main__":
    main()