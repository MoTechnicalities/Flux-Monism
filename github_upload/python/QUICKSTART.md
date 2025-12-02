# Python Quick Start

## Setup (One Time)

```bash
# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

## Run Demos

### Topology Analyzer
```bash
./run_flux_demo.sh
```
Shows particle topology table, path lengths, and mass predictions.

### 3D Visualizer (Basic)
```bash
./run_3d_generator.sh
```
Generates 11 .obj models and 11 .html previews in `output/`

### 3D Visualizer (Enhanced)
```bash
.venv/bin/python flux_monism_3d_enhanced.py
```
Generates enhanced visualizations with magnetic polarity colors in `output_enhanced/`

## View Results

**Interactive HTML previews:**
```bash
firefox output_enhanced/previews/electron_T2_1.html
```

**Import OBJ into Blender:**
1. Open Blender
2. File → Import → Wavefront (.obj)
3. Navigate to `output_enhanced/models/`
4. Select particle model

**Automated Blender rendering:**
```bash
blender --background --python output_enhanced/render_in_blender.py
```

## Files Overview

- `flux_monism_demo.py` - Main topology analyzer
- `flux_monism_3d.py` - Basic 3D generator
- `flux_monism_3d_enhanced.py` - Enhanced with magnetic colors
- `flux_monism_simple.py` - Quick topology table
- `run_flux_demo.sh` - Launcher for demo
- `run_3d_generator.sh` - Launcher for basic 3D

## Troubleshooting

**"ModuleNotFoundError: No module named 'numpy'"**
- Make sure virtual environment is activated: `source .venv/bin/activate`
- Or use launcher scripts which activate automatically

**"Permission denied" when running .sh files**
- Make executable: `chmod +x run_flux_demo.sh run_3d_generator.sh`

**Previews won't open**
- HTML files are large (~6-7 MB), may take a few seconds to load
- Try different browser if issues persist
