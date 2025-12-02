# FORTRAN Quick Start

## Compilation and Execution

### Linux/macOS
```bash
./run_fortran_demo.sh
```

### Manual Compilation
```bash
gfortran -o flux_monism_demo flux_monism_demo.f90
./flux_monism_demo
```

### Windows
```bash
gfortran.exe -o flux_monism_demo.exe flux_monism_demo.f90
flux_monism_demo.exe
```

## Installation

### Ubuntu/Debian
```bash
sudo apt-get install gfortran
```

### macOS
```bash
brew install gcc
```

### Fedora/RHEL
```bash
sudo dnf install gcc-gfortran
```

### Windows
Download MinGW-w64 or use WSL (Windows Subsystem for Linux)

## What It Does

The FORTRAN program calculates:
- Torus knot path lengths for T(p,q) topologies
- Mass predictions from path lengths
- Topology table for 11 fundamental particles
- Uses numerical integration with 100,000 points

**Performance**: Completes all calculations in < 1 second

## Output Interpretation

### Path Lengths
- Dimensionless geometric values
- Calculated via numerical integration
- Electron T(2,1): 12.7135
- Muon T(4,1): 25.2067 (1.98× electron)

### Mass Predictions
⚠️ **Important**: Absolute mass values are ~10⁵⁸ too large (dimensional calibration issue).

Focus on:
- Relative mass ordering (correct)
- Topological relationships (correct)
- Family patterns (correct)

The program demonstrates the **geometric framework**, not quantitative mass predictions.

## Differences from Python Version

- **Identical calculations**: Same formulas, same parameters
- **Same output**: Path lengths match to 4 decimal places
- **Performance**: FORTRAN is faster for large calculations
- **Dependencies**: None (no external libraries needed)
- **Portability**: Single self-contained file

## File Contents

- `flux_monism_demo.f90` - Main program (310 lines)
- `run_fortran_demo.sh` - Compilation and execution script

## Troubleshooting

**"command not found: gfortran"**
- Install gfortran compiler (see Installation above)

**"Error: Symbol 'r' already has basic type"**
- This was fixed in the current version
- Redownload if you have old version

**Compilation warnings**
- Warnings about unused variables are safe to ignore
- Code compiles with zero errors
