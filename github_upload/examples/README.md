# Example 3D Models

This directory contains sample 3D visualizations of particle topologies.

## Files Included

### Models (`.obj` format)
- `electron_T2_1.obj` - Electron topology T(2,1)
- `proton_T3_2.obj` - Proton topology T(3,2)
- `photon_T1_0.obj` - Photon topology T(1,0) (simple circle)

### Interactive Previews (`.html` format)
- `electron_T2_1.html` - Interactive electron visualization
- `proton_T3_2.html` - Interactive proton visualization
- `photon_T1_0.html` - Interactive photon visualization

## How to Use

### View in Browser
Simply open any `.html` file in a web browser:
```bash
firefox previews/electron_T2_1.html
```

**Controls:**
- **Left mouse drag**: Rotate
- **Scroll wheel**: Zoom
- **Right mouse drag**: Pan
- **Double click**: Reset view

### Import into Blender
1. Open Blender
2. File → Import → Wavefront (.obj)
3. Navigate to `models/` directory
4. Select desired particle file
5. The mesh will appear at origin

### Import into Other 3D Software
OBJ format is widely supported:
- Maya, 3ds Max, Cinema 4D
- Unity, Unreal Engine
- MeshLab, Mesh Mixer
- Most 3D printing software

## Color Coding

The enhanced models use magnetic polarity colors:

- **Electron**: Blue → Red (negative charge, right-hand rule)
- **Proton**: Red → Blue (positive charge, left-hand rule)
- **Photon**: Yellow symmetric (neutral)

Gradient direction encodes magnetic moment orientation.

## Generate More Models

To generate all 11 particle topologies:

```bash
cd ../python
./run_3d_generator.sh           # Basic version
# or
.venv/bin/python flux_monism_3d_enhanced.py  # Enhanced version
```

## File Sizes

- **OBJ files**: ~1.5 MB each (high resolution mesh)
- **HTML files**: ~6-7 MB each (includes Plotly.js library)

## Technical Details

- **Mesh resolution**: 1200 points along knot curve, 24 tube segments
- **Parametric equations**: Standard torus knot T(p,q)
- **Major radius**: R = 1.0
- **Minor radius**: a = 0.3
- **Variable thickness**: Based on curvature (enhanced version only)

## Viewing Tips

**HTML previews:**
- Files are large, may take 2-3 seconds to load
- Best viewed in Chrome, Firefox, or Edge
- Dark background optimized for knot visibility

**OBJ models in Blender:**
- Add lighting for better visualization
- Use HDRI environment for realistic rendering
- Materials included in enhanced Blender script

## License

[Same as parent project]
