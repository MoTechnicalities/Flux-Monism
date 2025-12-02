#!/usr/bin/env python3
"""
============================================================================
FLUX MONISM 3D VISUALIZER - ENHANCED VERSION
Generate beautiful 3D models with flux flow visualization
============================================================================

Enhanced features:
  - Color gradients showing flux flow direction
  - Variable tube thickness based on curvature
  - Particle-specific visual styling
  - Better aesthetics for presentations

Usage: 
  python3 flux_monism_3d_enhanced.py
  
Output:
  - output_enhanced/models/*.obj          (3D mesh files)
  - output_enhanced/previews/*.html       (Interactive previews)
  - output_enhanced/render_in_blender.py  (Blender script)
"""

import numpy as np
import os
import sys

# Universal constants
PI = np.pi

# Particle topology database with enhanced styling
# Color scheme follows magnetic polarity convention:
#   Negative charge: Blue (South) → Red (North) - Right-hand rule
#   Positive charge: Red (North) → Blue (South) - Left-hand rule  
#   Neutral: Symmetric or distinct color schemes
particles = [
    # name, p, q, spin, charge, type, color_start, color_end, glow_intensity
    ("Electron",    2, 1, 0.5, -1, "lepton", "#1e3a8a", "#dc2626", 1.2),  # Blue → Red (RH rule)
    ("Positron",    1, 2, 0.5, +1, "lepton", "#dc2626", "#1e3a8a", 1.2),  # Red → Blue (LH rule)
    ("Muon",        4, 1, 0.5, -1, "lepton", "#1e40af", "#ef4444", 1.3),  # Blue → Red (RH rule)
    ("Tau",         6, 1, 0.5, -1, "lepton", "#1e3a8a", "#f87171", 1.4),  # Blue → Red (RH rule)
    ("Proton",      3, 2, 0.5, +1, "hadron", "#dc2626", "#1e3a8a", 1.0),  # Red → Blue (LH rule)
    ("Neutron",     3, 4, 0.5,  0, "hadron", "#64748b", "#cbd5e1", 0.8),  # Gray neutral
    ("Lambda",      3, 5, 0.5,  0, "hadron", "#059669", "#6ee7b7", 0.9),  # Green neutral
    ("Sigma",       4, 3, 0.5,  0, "hadron", "#0d9488", "#5eead4", 0.9),  # Teal neutral
    ("Delta",       5, 2, 1.5, +2, "hadron", "#dc2626", "#3b82f6", 1.1),  # Red → Blue (positive)
    ("Omega",       5, 6, 1.5, -1, "hadron", "#2563eb", "#dc2626", 1.0),  # Blue → Red (negative)
    ("Photon",      1, 0, 1.0,  0, "boson",  "#fbbf24", "#fde047", 1.5),  # Yellow symmetric
]


def generate_torus_knot_mesh_enhanced(p, q, R=1.0, a=0.3, N=1200, tube_segments=24, base_radius=0.10):
    """
    Generate enhanced 3D mesh with variable thickness and better geometry.
    
    Args:
        p, q: Knot parameters
        R: Major radius
        a: Minor radius  
        N: Points along the knot curve (increased for smoothness)
        tube_segments: Circular segments for tube cross-section (increased)
        base_radius: Base thickness of the tube
        
    Returns:
        vertices: List of (x, y, z) coordinates
        faces: List of triangle indices
        colors: List of RGB colors for each vertex (for gradient)
    """
    if p == 1 and q == 0:  # Photon - glowing ring
        t = np.linspace(0, 2*PI, N)
        curve = np.column_stack([R * np.cos(t), R * np.sin(t), np.zeros(N)])
        # Photon has constant radius
        radius_variation = np.ones(N)
    else:
        # Standard torus knot parametric curve
        t = np.linspace(0, 2*PI, N, endpoint=False)
        x = (R + a * np.cos(q * t)) * np.cos(p * t)
        y = (R + a * np.cos(q * t)) * np.sin(p * t)
        z = a * np.sin(q * t)
        curve = np.column_stack([x, y, z])
        
        # Variable thickness based on curvature
        # Calculate curvature approximation
        tangents = np.roll(curve, -1, axis=0) - np.roll(curve, 1, axis=0)
        tangent_change = np.linalg.norm(np.roll(tangents, -1, axis=0) - tangents, axis=1)
        
        # Normalize and smooth
        curvature = tangent_change / (tangent_change.max() + 1e-8)
        # Apply smoothing
        try:
            from scipy.ndimage import gaussian_filter1d
            curvature_smooth = gaussian_filter1d(curvature, sigma=N//50, mode='wrap')
        except ImportError:
            # Fallback: simple moving average if scipy not available
            window = N//50
            curvature_smooth = np.copy(curvature)
            for i in range(N):
                start = (i - window) % N
                end = (i + window) % N
                if start < end:
                    curvature_smooth[i] = np.mean(curvature[start:end])
                else:
                    curvature_smooth[i] = np.mean(np.concatenate([curvature[start:], curvature[:end]]))
        except:
            # Final fallback
            curvature_smooth = curvature
        
        # Thickness varies: thicker at high curvature regions
        radius_variation = 1.0 + 0.3 * curvature_smooth
    
    # Compute tangent vectors
    tangents = np.roll(curve, -1, axis=0) - curve
    tangents = tangents / (np.linalg.norm(tangents, axis=1, keepdims=True) + 1e-8)
    
    # Compute normal vectors
    up = np.array([0, 0, 1])
    normals = np.cross(tangents, up)
    normals = normals / (np.linalg.norm(normals, axis=1, keepdims=True) + 1e-8)
    
    # Compute binormals
    binormals = np.cross(tangents, normals)
    binormals = binormals / (np.linalg.norm(binormals, axis=1, keepdims=True) + 1e-8)
    
    # Generate tube mesh with variable radius
    vertices = []
    colors = []
    
    theta = np.linspace(0, 2*PI, tube_segments, endpoint=False)
    
    for i in range(N):
        center = curve[i]
        normal = normals[i]
        binormal = binormals[i]
        tube_radius = base_radius * radius_variation[i]
        
        # Color gradient parameter (0 to 1 along curve)
        color_param = i / N
        
        # Create circular cross-section
        for j in range(tube_segments):
            offset = tube_radius * (np.cos(theta[j]) * normal + np.sin(theta[j]) * binormal)
            vertex = center + offset
            vertices.append(vertex)
            colors.append(color_param)  # Store gradient position
    
    # Create faces
    faces = []
    for i in range(N):
        for j in range(tube_segments):
            v1 = i * tube_segments + j
            v2 = i * tube_segments + (j + 1) % tube_segments
            v3 = ((i + 1) % N) * tube_segments + j
            v4 = ((i + 1) % N) * tube_segments + (j + 1) % tube_segments
            
            faces.append([v1, v2, v4])
            faces.append([v1, v4, v3])
    
    return np.array(vertices), np.array(faces), np.array(colors)


def export_to_obj(vertices, faces, filename):
    """Export mesh to Wavefront OBJ format"""
    with open(filename, 'w') as f:
        f.write(f"# Flux Monism Particle Topology (Enhanced)\n")
        f.write(f"# Generated by flux_monism_3d_enhanced.py\n\n")
        
        # Write vertices
        for v in vertices:
            f.write(f"v {v[0]:.6f} {v[1]:.6f} {v[2]:.6f}\n")
        
        f.write("\n")
        
        # Write faces (OBJ uses 1-based indexing)
        for face in faces:
            f.write(f"f {face[0]+1} {face[1]+1} {face[2]+1}\n")


def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple (0-1 range)"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))


def interpolate_color(color1, color2, t):
    """Interpolate between two hex colors"""
    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)
    return tuple(rgb1[i] * (1-t) + rgb2[i] * t for i in range(3))


def generate_plotly_html_enhanced(vertices, faces, colors, name, p, q, color_start, color_end, filename):
    """Generate enhanced interactive HTML preview with gradient colors"""
    try:
        import plotly.graph_objects as go
        import plotly.express as px
    except ImportError:
        print("Warning: plotly not installed. Skipping HTML preview generation.")
        return
    
    # Create color array for vertices
    vertex_colors = []
    for color_param in colors:
        rgb = interpolate_color(color_start, color_end, color_param)
        vertex_colors.append(f'rgb({int(rgb[0]*255)}, {int(rgb[1]*255)}, {int(rgb[2]*255)})')
    
    # Create mesh3d plot with vertex colors
    fig = go.Figure(data=[
        go.Mesh3d(
            x=vertices[:, 0],
            y=vertices[:, 1],
            z=vertices[:, 2],
            i=faces[:, 0],
            j=faces[:, 1],
            k=faces[:, 2],
            intensity=colors,  # Color intensity based on position
            colorscale=[[0, color_start], [1, color_end]],  # Gradient
            opacity=0.95,
            name=name,
            lighting=dict(
                ambient=0.4,
                diffuse=0.8,
                specular=0.6,
                roughness=0.3,
                fresnel=0.4
            ),
            lightposition=dict(x=100, y=100, z=100)
        )
    ])
    
    fig.update_layout(
        title=dict(
            text=f"<b>{name}</b> — T({p},{q}) Torus Knot<br>"
                 f"<i>Flux Monism Particle Topology (Enhanced Visualization)</i>",
            font=dict(size=20)
        ),
        scene=dict(
            xaxis=dict(
                title="X", 
                backgroundcolor="rgb(20, 20, 30)",
                gridcolor="rgb(50, 50, 60)",
                showbackground=True
            ),
            yaxis=dict(
                title="Y",
                backgroundcolor="rgb(20, 20, 30)",
                gridcolor="rgb(50, 50, 60)",
                showbackground=True
            ),
            zaxis=dict(
                title="Z",
                backgroundcolor="rgb(20, 20, 30)",
                gridcolor="rgb(50, 50, 60)",
                showbackground=True
            ),
            aspectmode='data',
            bgcolor="rgb(10, 10, 15)"
        ),
        paper_bgcolor="rgb(15, 15, 20)",
        width=1000,
        height=800,
    )
    
    fig.write_html(filename)


def generate_blender_script_enhanced(particle_list, output_dir):
    """Generate enhanced Blender Python script with better materials"""
    script = '''#!/usr/bin/env python3
"""
Blender Python Script: Render Enhanced Flux Monism Topologies
Generated by flux_monism_3d_enhanced.py

Features:
  - Gradient materials showing flux flow
  - Emission/glow effects
  - Better lighting setup
  - High-quality rendering

Usage in Blender:
  1. Open Blender
  2. Go to Scripting tab
  3. Open this file
  4. Click "Run Script"
"""

import bpy
import os
from mathutils import Vector

# Configuration
OUTPUT_DIR = "output_enhanced/renders"
MODEL_DIR = "output_enhanced/models"
IMAGE_SIZE = (1920, 1080)
SAMPLES = 256  # Higher quality

# Particle data: (name, p, q, color_start, color_end, glow)
PARTICLES = [
'''
    
    for name, p, q, spin, charge, ptype, color_start, color_end, glow in particle_list:
        script += f'    ("{name}", {p}, {q}, "{color_start}", "{color_end}", {glow}),\n'
    
    script += ''']

def setup_scene():
    """Setup enhanced rendering scene"""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    # Cycles renderer with high quality
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.cycles.samples = SAMPLES
    bpy.context.scene.render.resolution_x = IMAGE_SIZE[0]
    bpy.context.scene.render.resolution_y = IMAGE_SIZE[1]
    bpy.context.scene.cycles.use_denoising = True
    
    # Camera
    bpy.ops.object.camera_add(location=(4.5, -4.5, 3.5))
    camera = bpy.context.object
    camera.rotation_euler = (1.0, 0, 0.785)
    bpy.context.scene.camera = camera
    
    # Three-point lighting
    # Key light
    bpy.ops.object.light_add(type='AREA', location=(5, -3, 8))
    key = bpy.context.object
    key.data.energy = 300
    key.data.size = 4
    
    # Fill light
    bpy.ops.object.light_add(type='AREA', location=(-3, -5, 4))
    fill = bpy.context.object
    fill.data.energy = 150
    fill.data.size = 3
    
    # Rim light
    bpy.ops.object.light_add(type='AREA', location=(0, 5, 3))
    rim = bpy.context.object
    rim.data.energy = 200
    rim.data.size = 3
    
    # World background
    bpy.context.scene.world.use_nodes = True
    bg = bpy.context.scene.world.node_tree.nodes['Background']
    bg.inputs['Color'].default_value = (0.02, 0.02, 0.03, 1.0)
    bg.inputs['Strength'].default_value = 0.5

def hex_to_rgb(hex_color):
    """Convert hex to RGB"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))

def create_gradient_material(name, color_start, color_end, glow_strength):
    """Create gradient material with emission"""
    mat = bpy.data.materials.new(name=f"{name}_GradientMat")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    nodes.clear()
    
    # Output
    output = nodes.new('ShaderNodeOutputMaterial')
    output.location = (400, 0)
    
    # Mix shader (combines gradient and emission)
    mix = nodes.new('ShaderNodeMixShader')
    mix.location = (200, 0)
    
    # Principled BSDF
    bsdf = nodes.new('ShaderNodeBsdfPrincipled')
    bsdf.location = (0, 100)
    
    # Emission shader
    emission = nodes.new('ShaderNodeEmission')
    emission.location = (0, -100)
    
    # Color ramp for gradient
    ramp = nodes.new('ShaderNodeValToRGB')
    ramp.location = (-200, 0)
    
    # Texture coordinate for gradient
    coord = nodes.new('ShaderNodeTexCoord')
    coord.location = (-600, 0)
    
    # Gradient texture
    gradient = nodes.new('ShaderNodeTexGradient')
    gradient.location = (-400, 0)
    
    # Set colors
    rgb_start = hex_to_rgb(color_start)
    rgb_end = hex_to_rgb(color_end)
    
    ramp.color_ramp.elements[0].color = (*rgb_start, 1.0)
    ramp.color_ramp.elements[1].color = (*rgb_end, 1.0)
    
    # Configure BSDF
    bsdf.inputs['Metallic'].default_value = 0.4
    bsdf.inputs['Roughness'].default_value = 0.3
    bsdf.inputs['Specular'].default_value = 0.8
    
    # Configure emission
    emission.inputs['Strength'].default_value = glow_strength
    
    # Connect nodes
    links.new(coord.outputs['Object'], gradient.inputs['Vector'])
    links.new(gradient.outputs['Fac'], ramp.inputs['Fac'])
    links.new(ramp.outputs['Color'], bsdf.inputs['Base Color'])
    links.new(ramp.outputs['Color'], emission.inputs['Color'])
    links.new(bsdf.outputs['BSDF'], mix.inputs[1])
    links.new(emission.outputs['Emission'], mix.inputs[2])
    links.new(mix.outputs['Shader'], output.inputs['Surface'])
    
    mix.inputs['Fac'].default_value = 0.15  # 15% emission blend
    
    return mat

def import_and_render(name, p, q, color_start, color_end, glow):
    """Import and render with enhanced materials"""
    print(f"\\nRendering {name} T({p},{q})...")
    
    # Clear mesh objects
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            bpy.data.objects.remove(obj, do_unlink=True)
    
    # Import OBJ
    obj_file = os.path.join(MODEL_DIR, f"{name.lower()}_T{p}_{q}.obj")
    if not os.path.exists(obj_file):
        print(f"Warning: {obj_file} not found")
        return
    
    bpy.ops.import_scene.obj(filepath=obj_file)
    obj = bpy.context.selected_objects[0]
    
    # Apply gradient material
    mat = create_gradient_material(name, color_start, color_end, glow)
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)
    
    # Render
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_file = os.path.join(OUTPUT_DIR, f"{name.lower()}_enhanced.png")
    bpy.context.scene.render.filepath = output_file
    bpy.ops.render.render(write_still=True)
    
    print(f"Saved: {output_file}")

def main():
    """Main rendering loop"""
    print("=" * 70)
    print("FLUX MONISM - Enhanced Blender Renderer")
    print("=" * 70)
    
    setup_scene()
    
    for name, p, q, c_start, c_end, glow in PARTICLES:
        import_and_render(name, p, q, c_start, c_end, glow)
    
    print("\\n" + "=" * 70)
    print("Enhanced rendering complete!")
    print("=" * 70)

if __name__ == "__main__":
    main()
'''
    
    output_file = os.path.join(output_dir, "render_in_blender.py")
    with open(output_file, 'w') as f:
        f.write(script)
    
    os.chmod(output_file, 0o755)
    print(f"Created enhanced Blender script: {output_file}")


def main():
    """Main enhanced 3D generation pipeline"""
    print("=" * 85)
    print(" " * 15 + "FLUX MONISM 3D TOPOLOGY GENERATOR (ENHANCED)")
    print(" " * 20 + "With Flux Flow Visualization")
    print("=" * 85)
    print()
    
    # Create output directories
    output_dir = "output_enhanced"
    models_dir = os.path.join(output_dir, "models")
    previews_dir = os.path.join(output_dir, "previews")
    
    for directory in [output_dir, models_dir, previews_dir]:
        os.makedirs(directory, exist_ok=True)
    
    # Generate enhanced meshes
    for name, p, q, spin, charge, ptype, color_start, color_end, glow in particles:
        print(f"Generating enhanced {name} T({p},{q})...")
        
        # Generate 3D mesh with enhancements
        vertices, faces, colors = generate_torus_knot_mesh_enhanced(
            p, q, N=1200, tube_segments=24, base_radius=0.10
        )
        
        # Export to OBJ
        obj_filename = os.path.join(models_dir, f"{name.lower()}_T{p}_{q}.obj")
        export_to_obj(vertices, faces, obj_filename)
        print(f"  ✓ Exported: {obj_filename}")
        
        # Generate enhanced HTML preview
        html_filename = os.path.join(previews_dir, f"{name.lower()}_T{p}_{q}.html")
        generate_plotly_html_enhanced(
            vertices, faces, colors, name, p, q, 
            color_start, color_end, html_filename
        )
        if os.path.exists(html_filename):
            print(f"  ✓ Preview: {html_filename}")
    
    print()
    print("=" * 85)
    
    # Generate enhanced Blender script
    generate_blender_script_enhanced(particles, output_dir)
    
    print()
    print("ENHANCED GENERATION COMPLETE!")
    print("-" * 85)
    print(f"Enhanced OBJ models:       {models_dir}/")
    print(f"Enhanced HTML previews:    {previews_dir}/")
    print(f"Enhanced Blender script:   {output_dir}/render_in_blender.py")
    print()
    print("Enhancements:")
    print("  ✓ Color gradients showing flux flow direction")
    print("  ✓ Variable tube thickness (thicker at high curvature)")
    print("  ✓ Improved lighting and materials")
    print("  ✓ Particle-specific glow effects")
    print("  ✓ Smoother geometry (1200 points vs 1000)")
    print()
    print("Compare with original: output/ vs output_enhanced/")
    print("=" * 85)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGeneration interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
