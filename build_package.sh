#!/bin/bash
# Build script for TamilKavi package
# Run this script to clean, build, and prepare the package for upload

echo "🧹 Cleaning old build files..."
rm -rf build/ dist/ *.egg-info/

echo "📦 Building package..."
python -m build

if [ $? -eq 0 ]; then
    echo "✅ Package built successfully!"
    echo ""
    echo "📁 Built files in dist/:"
    ls -lh dist/
    echo ""
    echo "📤 To upload to PyPI, run:"
    echo "   python -m twine upload dist/*"
    echo ""
    echo "🧪 To test locally, run:"
    echo "   pip install dist/tamilkavi-0.7.0-py3-none-any.whl --force-reinstall"
else
    echo "❌ Build failed!"
    exit 1
fi

