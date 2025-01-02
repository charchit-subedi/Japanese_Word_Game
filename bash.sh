#!/bin/bash

VENV_DIR="venv"

# Set up virtual environment without printing anything
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR" >/dev/null 2>&1
fi

source "$VENV_DIR/bin/activate" >/dev/null 2>&1

# Upgrade pip without printing anything
pip install --upgrade pip >/dev/null 2>&1

# Install gTTS and pygame without printing anything
pip install gTTS >/dev/null 2>&1
pip install pygame >/dev/null 2>&1

# Check for installation errors (hidden unless it fails)
if [ $? -ne 0 ]; then
    echo "Failed to install required packages. Please check the error messages."
    exit 1
fi

# Run the Python script
python3 meaning.py

# Deactivate virtual environment
deactivate

