#!/bin/bash
# Flux Monism Demo Launcher
# Automatically uses the correct Python environment

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VENV_PYTHON="$SCRIPT_DIR/.venv/bin/python"

if [ ! -f "$VENV_PYTHON" ]; then
    echo "Error: Virtual environment not found at $VENV_PYTHON"
    echo "Please run: python3 -m venv .venv && .venv/bin/pip install numpy"
    exit 1
fi

exec "$VENV_PYTHON" "$SCRIPT_DIR/flux_monism_demo.py" "$@"
