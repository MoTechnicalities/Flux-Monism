# Flux Monism Computational Tools

Computational tools for exploring the Flux Monism theory from ["One Equation to Rule Them All"](https://rofick.com/ruling_equation/) by Mogir Jason Rofick.

## Theory Overview

Flux Monism proposes that:
- The universe consists of a single magnetic flux medium
- Particles are topological knots (torus knots) in this medium
- A single universal constant σ = 3.518×10⁴³ N determines all particle properties
- Particle topology T(p,q) encodes mass, spin, charge, and family structure

## Available Tools

### 🐍 Python Tools (`python/`)
- **`flux_monism_demo.py`** - Topology analyzer and mass predictor
- **`flux_monism_3d.py`** - Basic 3D mesh generator
- **`flux_monism_3d_enhanced.py`** - Enhanced visualizer with magnetic polarity colors
- **`flux_monism_simple.py`** - Quick topology reference table

### 🔧 FORTRAN Tools (`fortran/`)
- **`flux_monism_demo.f90`** - High-performance topology analyzer
- Identical calculations to Python version
- Compiles with standard gfortran

### 📊 Examples (`examples/`)
- Sample 3D models in .obj format (Blender compatible)
- Interactive HTML previews (rotate/zoom with mouse)
- Demonstrates electron, proton, and photon topologies

---

## Quick Start

### Python Demo
```bash
cd python
./run_flux_demo.sh
```

### Generate 3D Visualizations
```bash
cd python
./run_3d_generator.sh
```
Outputs to `output/` (basic) and `output_enhanced/` (with magnetic polarity colors)

### FORTRAN Demo
```bash
cd fortran
./run_fortran_demo.sh
```

### View Interactive 3D Preview
```bash
# Open any HTML file in examples/previews/ with a web browser
firefox ../examples/previews/electron_T2_1.html
```

---

## Installation

### Python Requirements
```bash
cd python
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

**Dependencies**: NumPy, Plotly

### FORTRAN Requirements
```bash
# Ubuntu/Debian
sudo apt-get install gfortran

# macOS
brew install gcc

# Fedora/RHEL
sudo dnf install gcc-gfortran
```

---

## What the Programs Demonstrate

### ✅ Working Features
- **Topological classification**: All particles assigned T(p,q) knot topology
- **Path length calculations**: Numerical integration of knot geometry
- **Family patterns**: Leptons follow T(2n,1), antiparticles are inverted T(q,p)
- **Mass ordering**: More complex knots → longer paths → greater mass
- **Single parameter**: Only σ determines all structure
- **3D visualization**: Interactive models with magnetic polarity encoding

### ⚠️ Known Limitations
- **Mass scale**: Absolute predictions are ~10⁵⁸ too large (dimensional calibration issue)
- **Mass ratios**: Path length ratios don't directly match experimental mass ratios
- **Interpretation**: Topology influences mass, but relationship is not simple proportionality

The tools demonstrate the **geometric framework** while acknowledging quantitative refinement is needed.

---

## Particle Topology Table

| Particle | Topology | Spin | Charge | Type   |
|----------|----------|------|--------|--------|
| Electron | T(2,1)   | 0.5  | -1     | Lepton |
| Positron | T(1,2)   | 0.5  | +1     | Lepton |
| Muon     | T(4,1)   | 0.5  | -1     | Lepton |
| Tau      | T(6,1)   | 0.5  | -1     | Lepton |
| Proton   | T(3,2)   | 0.5  | +1     | Hadron |
| Neutron  | T(3,4)   | 0.5  | 0      | Hadron |
| Lambda   | T(3,5)   | 0.5  | 0      | Hadron |
| Sigma    | T(4,3)   | 0.5  | 0      | Hadron |
| Delta    | T(5,2)   | 1.5  | +2     | Hadron |
| Omega    | T(5,6)   | 1.5  | -1     | Hadron |
| Photon   | T(1,0)   | 1.0  | 0      | Boson  |

---

## 3D Visualization Color Scheme

The enhanced visualizer uses **magnetic polarity colors** following electromagnetic conventions:

- **Negative particles** (e⁻, μ⁻, τ⁻, Ω⁻): Blue → Red (right-hand rule)
- **Positive particles** (e⁺, p⁺, Δ⁺⁺): Red → Blue (left-hand rule)
- **Neutral particles**: Distinct color schemes (gray, green, teal, yellow)

Gradient direction visually encodes the magnetic moment orientation.

---

## File Formats

### OBJ Models (`.obj`)
- Standard Wavefront 3D mesh format
- Import into Blender, Maya, 3ds Max, etc.
- ~1.5 MB per file (high resolution: 1200 points)

### HTML Previews (`.html`)
- Self-contained interactive visualizations
- Powered by Plotly.js
- Works in any modern web browser
- Supports rotation, zoom, pan
- ~6-7 MB per file

---

## Contributing

This is a theoretical physics exploration tool. Contributions welcome for:
- Performance optimizations
- Additional visualization features
- Physical insights on mass calibration
- Documentation improvements

---

## Citation

If you use these tools in research or education, please cite:

> Rofick, M.J. (2025). "One Equation to Rule Them All: A Unified Field Theory from Magnetic Flux Monism." 
> Available at: https://rofick.com/ruling_equation/

---

## License

[Specify your license here]

## Contact

- Website: https://rofick.com
- Repository: https://github.com/MoTechnicalities/Flux-Monism

---

## Acknowledgments

Computational tools developed to explore and visualize the topological framework proposed in Flux Monism theory.
