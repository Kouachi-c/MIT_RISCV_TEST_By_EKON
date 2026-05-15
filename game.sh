#!/bin/bash

# Check if Python3 is installed
if ! command -v python3 &>/dev/null; then
    echo "Python3 not found. Installing..."
    sudo apt-get update -qq && sudo apt-get install -y python3
fi

# Check if tkinter is available (standard library but sometimes missing on Linux)
if ! python3 -c "import tkinter" &>/dev/null; then
    echo "tkinter not found. Installing..."
    sudo apt-get install -y python3-tk
fi

# Launch the program
cd "$(dirname "$0")"
python3 main.py
