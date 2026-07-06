# Micro-to-Macro Bridge Worked Example: alpha_s(mu) v0.1.1

Concrete instantiation of `MICRO_TO_MACRO_BRIDGE_V0_1.md` for the strong coupling observable family.

## 1. Scope

This note operationalizes the bridge for one observable:

$$
O_k(\mu) \equiv \alpha_s(\mu)
$$

Goal: show a traceable decomposition into [Derived], [Calibrated], and [Conjectural] components with no hidden fit steps.

## 2. Model Decomposition for alpha_s

Use the bridge template:

$$
\alpha_s(\mu) = f_{\alpha}(\mathbf I,\mathbf P_0) + d_{\alpha}(\mu) + c_{\alpha}(\mu;\hat\theta_C) + q_{\alpha}(\mu;\theta_Q)
$$

For the current repository formulation, this is represented as:

$$
\alpha_s(Q) = \frac{c_0}{K(Q)}, \quad K(Q)=K_0\left(\frac{Q}{\Lambda_{\mathrm{QCD}}}\right)^{\gamma}
$$

and equivalently:

$$
\alpha_s(Q)=\alpha_0\left(\frac{\Lambda_{\mathrm{QCD}}}{Q}\right)^{\gamma},\quad \alpha_0 = \frac{c_0}{K_0}
$$

with the repository's current nominal values:

- $K_0 = 4.06$
- $c_0 = 1.42$
- $\alpha_0 \approx 0.35$
- $\Lambda_{\mathrm{QCD}} = 200\,\mathrm{MeV}$
- $\gamma \approx 3/(4\pi) \approx 0.239$

## 3. Status Tag Assignment

### 3.1 [Derived] terms

- Structural relation $\alpha_s \propto 1/K$ from confinement-strength interpretation.
- Dimensionless power-law form in $Q/\Lambda_{\mathrm{QCD}}$.
- Mapping consistency requirement: one invariant state must explain all sampled scales.

### 3.2 [Calibrated] terms

- $c_0$ and $K_0$ normalization at hadronic anchor scale.
- Numerical value of $\Lambda_{\mathrm{QCD}}$ used in the fit.
- Empirical fit of $\gamma$ from selected data window.

### 3.3 [Conjectural] terms

- Identification $\gamma = 3/(4\pi)$ as a topology-color relation beyond pure regression.
- Extrapolation outside the validated window (for example, deep UV and near-confinement edge).

## 4. Partition Protocol (A, D, P)

To avoid post hoc leakage, define disjoint sets.

### 4.1 Anchor set A (fit only calibrated parameters)

Use two anchors:

- A1: $\alpha_s(1\,\mathrm{GeV}) = 0.350$
- A2: $\alpha_s(M_Z=91.2\,\mathrm{GeV}) = 0.1179$

Fit parameters in A:

- $\hat\alpha_0$
- $\hat\gamma$

Then map to $(\hat c_0,\hat K_0,\hat\Lambda_{\mathrm{QCD}})$ with one chosen convention.

### 4.2 Derivation set D (no new fit)

Internal-consistency checks from theory structure:

- D1: monotone decrease $d\alpha_s/dQ < 0$
- D2: positivity $\alpha_s(Q)>0$
- D3: asymptotic trend $\lim_{Q\to\infty}\alpha_s(Q)=0$

### 4.3 Prediction set P (blind evaluation)

Hold out intermediate scales:

- P1: $Q=2\,\mathrm{GeV}$
- P2: $Q=5\,\mathrm{GeV}$
- P3: $Q=10\,\mathrm{GeV}$
- P4: $Q=34\,\mathrm{GeV}$

Success metrics:

- Relative error per point
- Weighted RMSE in log-space
- Residual trend test versus $\log Q$

## 5. Worked Numeric Snapshot (using current nominal values)

Model:

$$
\alpha_s(Q)=0.35\left(\frac{0.2}{Q}\right)^{0.239}
$$

with $Q$ in GeV.

Predictions:

- $\alpha_s(2)\approx 0.202$
- $\alpha_s(5)\approx 0.162$
- $\alpha_s(10)\approx 0.138$
- $\alpha_s(34)\approx 0.104$

Interpretation:

- This snapshot is a method demonstration of bridge bookkeeping.
- It is not yet a locked validation result because Anchor/Prediction partitions must be frozen before fit publication.

## 6. Falsification Gates for This Worked Example

The worked bridge for $\alpha_s$ fails if any gate is tripped:

1. No parameter set fits anchors while preserving monotone asymptotic behavior.
2. Holdout residuals show statistically significant scale trend.
3. Inferred $\gamma$ becomes unstable under small anchor perturbations.
4. A simpler baseline model outperforms bridge predictions on the holdout set.

## 7. Reproducibility Checklist

Before declaring v0.2 results, publish:

- Exact data source/version used for each $\alpha_s(Q)$ point.
- Fit objective and weights.
- Anchor/Prediction split committed before fitting.
- Parameter covariance matrix.
- Residual plots versus $Q$ and $\log Q$.

### Scripted Reproduction (Repository Tool)

Generate a markdown holdout report using the bundled script:

```bash
cd tools/python
./run_alpha_s_bridge_holdout.sh --out ../../alpha_s_holdout_report.md
```

This produces:

- `alpha_s_holdout_report.md`

which can be versioned alongside this worked example.

Current generated artifact in this workspace:

- [alpha_s_holdout_report.md](alpha_s_holdout_report.md)

## 8. Integration Back Into Main Manuscript

For Section 16 and falsification tables:

- Label alpha_s-related claims as [Calibrated] unless held-out prediction performance is published.
- Promote to [Derived] only for structural statements proven independent of fit constants.
- Keep topology-color closure $\gamma=3/(4\pi)$ as [Conjectural] until independently constrained.

---

Status: Worked example v0.1.1 (method instantiated, validation lock protocol defined).
