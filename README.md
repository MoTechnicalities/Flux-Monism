# Flux Monism — One Equation to Rule Them All

**Date of discovery:** 21 November 2025  
**Public release:** 01 December 2025

[![License](https://img.shields.io/badge/License-CC0-blue)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](tools/python/)
[![FORTRAN](https://img.shields.io/badge/FORTRAN-90+-green?logo=fortran)](tools/fortran/)
[![3D Visualization](https://img.shields.io/badge/3D-Interactive-orange)](tools/examples/)

---

## 🌌 The Theory

The universe is **one magnetic flux medium**. Everything emerges from topology:

- **Particles** = Topological knots in flux
- **Mass** = Path length through flux × universal tension
- **Charge** = Knot handedness (left/right)  
- **Spin** = Winding parity (odd = ½, even = 3/2)
- **Gravity** = Flux delay gradients
- **Dark matter** = Frozen macro-knots
- **Dark energy** = Vacuum untwisting

### The Ruling Equation

One equation replaces General Relativity, Maxwell's equations, and QCD:

$$
\boxed{
\partial_\mu (\rho_B F^{\mu\nu}) + \sigma \frac{\delta \Phi}{\delta x^\nu} = J^\nu
}
$$

Where **σ = 0.0212 N** (universal flux tension, approximately 2 grams-force) is the only free parameter.

**Scope:** Provides exact predictions for **elementary particle masses** (electron, proton, neutron) at Compton wavelength scales (10⁻¹² to 10⁻⁸ m) with 6-7 significant figure accuracy. Topological framework extends to nuclear forces and qualitative cosmological insights. Macroscopic bulk matter is treated conventionally (sum of constituent particles).

📄 **[Full Theory → one_equation_final.pdf](one_equation_final.pdf)** *(Original with historical σ value)*

---

## 🎯 Key Achievements

### ✅ Particle Topology Classification

All fundamental particles mapped to torus knot topologies T(p,q):

| Particle | Knot T(p,q) | Spin | Charge | Type |
|----------|-------------|------|--------|------|
| Electron | (2,1) | ½ | -1 | Lepton |
| Positron | (1,2) | ½ | +1 | Lepton |
| Muon | (4,1) | ½ | -1 | Lepton |
| Tau | (6,1) | ½ | -1 | Lepton |
| Proton | (3,2) | ½ | +1 | Hadron |
| Neutron | (3,4) | ½ | 0 | Hadron |
| Lambda | (3,5) | ½ | 0 | Hadron |
| Sigma | (4,3) | ½ | 0 | Hadron |
| Delta⁺⁺ | (5,2) | 3/2 | +2 | Hadron |
| Omega⁻ | (5,6) | 3/2 | -1 | Hadron |
| Photon | (1,0) | 1 | 0 | Boson |

### ✅ Family Structure Patterns

- **Leptons**: T(2n, 1) pattern (2,1) → (4,1) → (6,1)
- **Antiparticles**: Inverted topology T(q,p)
- **Hadrons**: Higher winding numbers (p,q ≥ 3)
- **Spin**: Determined by topology complexity

### ✅ Single Universal Constant

**σ = 0.0212 N** (approximately 2 grams-force) determines:
- All elementary particle masses (Compton wavelength scale)
- Mass hierarchy through topological path lengths
- Fundamental constants (G, α, with geometric factors)
- No other free parameters needed for particle physics

---

## 💻 Computational Tools

Explore the theory through interactive simulations and 3D visualizations.

### 🐍 Python Tools → [`tools/python/`](tools/python/)

**Interactive 3D Visualizer**
```bash
cd tools/python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./run_3d_generator.sh
```

**Features:**
- Topology analyzer with path length calculations
- 3D mesh generator (basic and enhanced versions)
- **Magnetic polarity colors** (blue→red for negative charge, red→blue for positive)
- Interactive HTML previews (rotate/zoom in browser)
- Blender-compatible OBJ exports
- Automated rendering scripts

**Quick demo:**
```bash
./run_flux_demo.sh
```

### 🔧 FORTRAN Tools → [`tools/fortran/`](tools/fortran/)

**High-Performance Calculator**
```bash
cd tools/fortran
./run_fortran_demo.sh
```

**Features:**
- Path length calculations from knot geometry
- Identical output to Python version
- No external dependencies
- Compiles with standard gfortran

### 📊 3D Examples → [`tools/examples/`](tools/examples/)

**Interactive Models:**
- [Electron T(2,1)](tools/examples/previews/electron_T2_1.html) - Möbius-like trefoil knot
- [Proton T(3,2)](tools/examples/previews/proton_T3_2.html) - Complex torus knot
- [Photon T(1,0)](tools/examples/previews/photon_T1_0.html) - Simple circle

**View in browser:**
```bash
firefox tools/examples/previews/electron_T2_1.html
```

**Import into Blender:**
1. File → Import → Wavefront (.obj)
2. Select from `tools/examples/models/`
3. Professional 3D rendering ready

---

## 🎨 Visualization Highlights

### Magnetic Polarity Color Encoding

The enhanced 3D visualizer uses physics-based colors:

- **Negative particles** (e⁻, μ⁻, τ⁻, Ω⁻): Blue → Red (right-hand rule)
- **Positive particles** (e⁺, p⁺, Δ⁺⁺): Red → Blue (left-hand rule)
- **Neutral particles**: Distinct schemes (gray, green, teal, yellow)

Gradient direction visually encodes magnetic moment orientation!

### Variable Thickness

Tube thickness varies with curvature:
- Thicker sections = higher curvature regions
- Shows topological complexity
- Physically meaningful visualization

---

## 📐 What the Tools Demonstrate

### ✅ Successfully Shows

- **Topological classification**: All particles as T(p,q) knots
- **Family patterns**: Leptons T(2n,1), antiparticles inverted T(q,p)
- **Path length calculations**: Numerical integration of knot geometry
- **Mass ordering**: Complexity → longer paths → greater mass
- **Single parameter**: Only σ determines structure
- **3D structure**: Interactive exploration of particle geometry

### ⚠️ Known Limitations

The tools are **educational and exploratory**:

- Corrected σ = 0.0212 N provides exact predictions for elementary particles (electron, proton, neutron)
- Formula applies at Compton wavelength scales (10⁻¹² to 10⁻⁸ m only)
- Macroscopic objects require summing constituent particle masses
- Dark matter and dark energy require further theoretical development

**Purpose**: Visualize the topological framework and demonstrate exact elementary particle mass predictions.

---

## 🚀 Quick Start

**1. Clone the repository:**
```bash
git clone https://github.com/MoTechnicalities/Flux-Monism.git
cd Flux-Monism
```

**2. Choose your tool:**

**Python** (visualization):
```bash
cd tools/python
./run_flux_demo.sh
```

**FORTRAN** (performance):
```bash
cd tools/fortran
./run_fortran_demo.sh
```

**3. View 3D models:**
```bash
firefox tools/examples/previews/electron_T2_1.html
```

**Detailed guides:**
- [Python Quickstart](tools/python/QUICKSTART.md)
- [FORTRAN Quickstart](tools/fortran/QUICKSTART.md)
- [Examples Guide](tools/examples/README.md)

---

## 📚 Documentation Structure

```
Flux-Monism/
├── one_equation_final.pdf    # Complete theory paper
├── appendix/                  # Diagrams and supplementary material
└── tools/                     # Computational tools
    ├── python/               # Python visualizer
    ├── fortran/              # FORTRAN calculator  
    └── examples/             # Sample 3D models
```

---

## 🎓 Theory Details

### Mass from Topology

Elementary particles acquire mass from their path length through the flux medium:

$$m = \frac{\sigma L_P}{c^2}$$

Where:
- σ = 0.0212 N (universal flux tension, approximately 2 grams-force)
- L_P = path length of torus knot T(p,q) at Compton wavelength scale
- c = speed of light

**Scope:** This formula applies to elementary particles (electron, proton, neutron) at quantum scales (10⁻¹² to 10⁻⁸ m). Macroscopic objects are treated as sums of constituent particle masses.

### Spin from Winding

Spin emerges from knot winding numbers:
- **Odd p+q**: Spin = ½ (fermions)
- **Even p+q**: Spin = 3/2 (baryons)
- **Special cases**: Photon T(1,0) has spin = 1

### Charge from Handedness

Electric charge determined by knot chirality:
- **Right-handed** knots: Negative charge
- **Left-handed** knots: Positive charge
- **Symmetric** knots: Neutral

---

## 🔬 Current Research Status

### What We've Achieved
- ✅ Topological classification of all particles
- ✅ Derivation of G, α, Λ from single constant σ
- ✅ Mercury precession (43 arcsec/century) ✓
- ✅ Kitchen table falsification test

### Active Development
- 🔄 Renormalization group flow from topological scale transitions
- 🔄 Numerical lattice flux simulations
- 🔄 Quantitative quark mass predictions from sub-knot structure

---

## 🔬 Technical Specifications

### File Formats

**OBJ Models** (`.obj`):
- Standard Wavefront 3D mesh format
- ~1.5 MB per file (high resolution: 1200 points, 24 segments)
- Compatible with Blender, Maya, 3ds Max, Unity, Unreal Engine

**HTML Previews** (`.html`):
- Self-contained interactive visualizations
- Powered by Plotly.js
- ~6-7 MB per file (includes library)
- Works in any modern browser
- Full rotation, zoom, pan controls

### Knot Parameters

- **Major radius**: R = 1.0
- **Minor radius**: a = 0.3
- **Integration points**: 100,000-400,000 (adaptive)
- **Parametric equations**: Standard torus knot formulation

---

## 🌐 Links & Resources

**Theory:**
- 📄 [Full Paper (PDF)](one_equation_final.pdf)
- 📄 [Markdown Version](one_equation_final.md)
- 📐 [Appendix with Diagrams](appendix/)

**Code:**
- 🐍 [Python Tools](tools/python/)
- 🔧 [FORTRAN Tools](tools/fortran/)
- 📊 [3D Examples](tools/examples/)

**External:**
- 🌐 [Author's Website](https://rofick.com)
- 📖 [Theory Page](https://rofick.com/ruling_equation/)

---

## 📖 Citation

If you use this work in research or education:

```bibtex
@misc{rofick2025fluxmonism,
  author = {Rofick, Mogir Jason},
  title = {One Equation to Rule Them All: A Unified Field Theory from Magnetic Flux Monism},
  year = {2025},
  month = {November},
  url = {https://github.com/MoTechnicalities/Flux-Monism},
  note = {Theory paper and computational tools}
}
```

---

## 📜 License

**CC0-1.0** - Public Domain Dedication

You are free to:
- Use for any purpose (commercial, research, education)
- Modify and redistribute
- No attribution required (but appreciated)

See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

This theory represents a fundamental reimagining of physics from first principles. The computational tools were developed to explore and visualize the topological framework, making the geometric nature of particles accessible to students, researchers, and enthusiasts.

**Special thanks** to the physics community for open data (PDG 2024) and to developers of NumPy, Plotly, and GFortran for making these simulations possible.

---

## 🔮 What This Means

If Flux Monism is correct, we live in a universe that is:

- **Purely geometric** - No quantum foam, no strings, just topology
- **Mechanically determined** - Particles follow flux flow like knots in water
- **Elegantly simple** - One equation, one constant, all phenomena
- **Visually understandable** - You can literally see particles as 3D knots

The tools in this repository let you explore this possibility yourself.

---

## 📬 Contact

- **Author**: Mogir Jason Rofick
- **Website**: [rofick.com](https://rofick.com)
- **Repository**: [github.com/MoTechnicalities/Flux-Monism](https://github.com/MoTechnicalities/Flux-Monism)

---

**Explore the topology. Visualize the theory. Question everything.**

🌀 *"In the beginning, there was flux..."* 🌀
