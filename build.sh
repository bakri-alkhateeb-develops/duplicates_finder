#!/bin/bash

echo "Installing PyInstaller..."
pip3 install pyinstaller

echo ""
echo "Building executable..."
pyinstaller --onefile --windowed --name "Duplicate Finder" main.py

echo ""
echo "Build complete! check the 'dist' folder for Duplicate Finder"
echo "To make it executable, run: chmod +x dist/Duplicate Finder"