## alpha_s Holdout Residual Report

### Model Lock

- Model: `alpha_s(Q) = alpha0 * (Lambda/Q)^gamma`
- Lambda_QCD (GeV): `0.200000`
- Anchor A1: `Q=1.000 GeV, alpha_s=0.350000`
- Anchor A2: `Q=91.200 GeV, alpha_s=0.117900`
- Fitted model alpha0: `0.515929`
- Fitted model gamma: `0.241100`
- Nominal model alpha0: `0.350000`
- Nominal model gamma: `0.238732`

### Holdout Results

| Q (GeV) | alpha_obs | alpha_pred_fit | alpha_pred_nominal | resid_fit | rel_fit | resid_nominal | rel_nominal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2.0 | 0.300000 | 0.296135 | 0.201993 | -0.003865 | -1.288% | -0.098007 | -32.669% |
| 5.0 | 0.214000 | 0.237436 | 0.162306 | +0.023436 | +10.951% | -0.051694 | -24.156% |
| 10.0 | 0.180000 | 0.200895 | 0.137553 | +0.020895 | +11.608% | -0.042447 | -23.582% |
| 34.0 | 0.137000 | 0.149565 | 0.102704 | +0.012565 | +9.171% | -0.034296 | -25.034% |

### Metrics (Fitted Model)

- RMSE (absolute alpha_s): `0.017019`
- RMSE (relative): `9.226%`
- RMSE (log residual): `0.087648`
- Weighted RMSE (absolute): `0.017586`
- Residual trend slope vs log(Q): `+0.032535`

### Metrics (Nominal Model)

- RMSE (absolute alpha_s): `0.061757`
- RMSE (relative): `26.616%`
- RMSE (log residual): `0.311553`
- Weighted RMSE (absolute): `0.041612`
- Residual trend slope vs log(Q): `+0.023962`

### Side-by-Side Comparison

- Delta RMSE_abs (nominal - fitted): `+0.044738`
- Delta RMSE_rel% (nominal - fitted): `+17.390%`
- Delta weighted RMSE (nominal - fitted): `+0.024026`
- Delta trend slope (nominal - fitted): `-0.008573`

Interpretation note:
- Near-zero residual slope supports the bridge criterion of no scale-trending holdout residuals.
- Lower RMSE and lower weighted RMSE indicate better holdout fit quality.
- This report is fully determined by the model lock and selected A/P partition.
