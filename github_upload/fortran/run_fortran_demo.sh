#!/bin/bash
# ============================================================================
# Launcher script for FORTRAN Flux Monism Demo
# ============================================================================

echo "Compiling FORTRAN version..."
gfortran -o flux_monism_demo flux_monism_demo.f90

if [ $? -eq 0 ]; then
    echo "Compilation successful! Running..."
    echo ""
    ./flux_monism_demo
else
    echo "ERROR: Compilation failed"
    echo "Make sure gfortran is installed: sudo apt-get install gfortran"
    exit 1
fi
