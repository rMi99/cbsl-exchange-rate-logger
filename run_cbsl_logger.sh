#!/bin/bash

# Change to script directory
cd "$(dirname "$0")"

# Create venv if it doesn't exist
if [ ! -d "venv" ]; then
    echo "[INFO] Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements only if not already installed
if [ ! -f "venv/.pip_installed" ]; then
    echo "[INFO] Installing dependencies..."
    pip install -r requirements.txt && touch venv/.pip_installed
else
    echo "[INFO] Requirements already installed, skipping pip install."
fi

# Run the script
echo "[INFO] Running CBSL logger..."
python3 cbsl_logger.py
