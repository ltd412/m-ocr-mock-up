#!/bin/bash
set -e

# Clean up previous builds
echo "Cleaning up..."
rm -rf build dist *.egg-info

# Build the package
echo "Building package..."
python3 -m pip install --upgrade build
python3 -m build

# Check the package
echo "Checking package..."
python3 -m pip install --upgrade twine
python3 -m twine check dist/*

echo "Build complete. To upload to PyPI, run:"
echo "python3 -m twine upload dist/*"
