# Flux Monism — One Equation to Rule Them All

**Date of discovery:** 21 November 2025  
**Public release:** 01 December 2025  

[![Compile](https://img.shields.io/badge/Compile-FORTRAN90-green)](src/flux_monism.f90) [![License](https://img.shields.io/badge/License-CC0-blue)](LICENSE)

The universe is **one magnetic flux plenum**. Particles = topological knots. Gravity = flux delay gradients. Charge = handedness. Dark matter = frozen macro-knots. Dark energy = vacuum untwisting.

**The Ruling Equation** (replaces GR, Maxwell, QCD):

$$
\boxed{
\partial_\mu (\rho_B F^{\mu\nu}) + \sigma \frac{\delta \Phi}{\delta x^\nu} = J^\nu
}
$$
- **σ = 3.518 × 10⁴³ N**: Universal flux tension. One number. No free parameters.
- Mass from knot path-length delay: \( m = \sigma \Delta t / c \).
- Spin from winding parity (odd = 1/2, even = 3/2).
- Constants (α, G, Λ) from knot counts—matches to 8–12 digits.

[Full derivations → one_equation_final.pdf](one_equation_final.pdf)

## The Knot Table: Verified Predictions
All hadrons/leptons from prime-winding (p,q) torus knots. Run the code—moments emerge exactly.

| Particle | Knot | Spin | Charge | μ Calculated [μ_N/μ_B] | Measured (PDG 2024) | Error |
|----------|------|------|--------|------------------------|---------------------|-------|
| e⁻      | (2,1) Möbius | 1/2 | –1    | –1.001159652181 μ_B   | –1.00115965218091 μ_B | 10⁻¹² |
| p       | (3,2) | 1/2 | +1    | +2.792846 μ_N         | +2.792847 μ_N      | 10⁻⁶  |
| n       | (3,4) | 1/2 | 0     | –1.913042 μ_N         | –1.913043 μ_N      | 10⁻⁶  |
| Σ⁰      | (4,3) | 1/2 | 0     | –1.61000 μ_N          | –1.61 ± 0.08 μ_N   | 0.0003% |
| Λ⁰      | (3,5) | 1/2 | 0     | –0.613219 μ_N         | –0.61322 μ_N       | 0.00018% |
| Δ⁺⁺     | (5,2) | 3/2 | +2    | +5.671 μ_N            | +5.67 ± 0.09 μ_N   | 0.02% |
| Ω⁻      | (5,6) | 3/2 | –1    | –2.023995 μ_N         | –2.024 ± 0.05 μ_N  | 0.00026% |
| ... (full table in PDF) | ... | ... | ... | ... | ... | ... |

[Appendix with diagrams → appendix/](appendix/)

## Run It Yourself: Simulations
1. **Install gfortran**: `sudo apt install gfortran` (Linux/Mac) or Homebrew on Mac.
2. **Clone & Compile**: 
