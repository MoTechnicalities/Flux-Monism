# Flux Monism Topology Tools

**Note**: These tools are distinct from the validated magnetic moment predictor in `src/`. 
The magnetic moment code achieves 10⁻⁶ accuracy. These topology tools focus on 
**visualization and geometric understanding** rather than precise quantitative predictions.

## What These Tools Do

### ✅ Successfully Demonstrates
- Topological classification of all particles as T(p,q) knots
- Family structure patterns (leptons: T(2n,1), antiparticles: inverted)
- Path length calculations from knot geometry
- Mass ordering follows topological complexity
- 3D visualization with magnetic polarity colors
- Interactive exploration of knot structures

### ⚠️ Known Limitations
- Absolute mass predictions are dimensionally incorrect (~10⁵⁸ too large)
- Path length ratios don't directly match experimental mass ratios
- These tools demonstrate the **framework**, not quantitative physics

## Complementary to Main Code

**`src/flux_monism.f90`** (magnetic moments):
- Uses area and flux current calculations
- Achieves experimental accuracy
- Validated against PDG 2024 data

**`tools/`** (this directory):
- Uses path length and topology
- Educational and exploratory
- Visualizes the knot structures

Both use σ = 3.518×10⁴³ N but tackle different problems.

---

## Installation and Usage

See subdirectories:
- `python/` - Python visualization tools
- `fortran/` - FORTRAN path length calculator  
- `examples/` - Sample 3D models

Each has its own QUICKSTART.md.

---

## Why Include These Tools?

1. **Visualization**: The theory is geometric - people need to SEE the knots
2. **Accessibility**: Python tools are easier for students/researchers to run
3. **Exploration**: Interactive 3D helps understand topology-mass relationships
4. **Framework**: Shows the classification system even where quantitative predictions need work
5. **Magnetic colors**: Encodes right-hand rule and charge in gradient direction

Think of these as "scaffolding" - they help understand the structure even if 
the mass calibration requires further theoretical development.

---

## Quick Start

**Python 3D Visualizer:**
```bash
cd python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./run_3d_generator.sh
```

**View Results:**
```bash
firefox output_enhanced/previews/electron_T2_1.html
```

**Import into Blender:**
- File → Import → Wavefront (.obj)
- Select from `output_enhanced/models/`

---

## Acknowledgment

These tools were developed to explore and visualize the topological framework 
described in "One Equation to Rule Them All." They complement but do not 
replace the validated magnetic moment calculations in `src/`.
