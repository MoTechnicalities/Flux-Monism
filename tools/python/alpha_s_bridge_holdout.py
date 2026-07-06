#!/usr/bin/env python3
"""Compute alpha_s(Q) holdout residual metrics for the micro-to-macro bridge.

This script fits a two-parameter power law from anchor points:
    alpha_s(Q) = alpha0 * (Lambda / Q)^gamma

Then it evaluates holdout points and emits a markdown report that can be pasted
into MICRO_TO_MACRO_BRIDGE_WORKED_EXAMPLE_ALPHA_S_V0_1_1.md.

No external dependencies required.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Dict, List, Sequence, Tuple


@dataclass(frozen=True)
class DataPoint:
    q_gev: float
    alpha_obs: float
    sigma_obs: float


def parse_points(raw: Sequence[str], label: str) -> List[Tuple[float, float]]:
    points: List[Tuple[float, float]] = []
    for item in raw:
        try:
            q_str, a_str = item.split(":", 1)
            q_val = float(q_str)
            a_val = float(a_str)
        except ValueError as exc:
            raise ValueError(
                f"Invalid {label} point '{item}'. Expected format Q:alpha, e.g. 1.0:0.350"
            ) from exc
        if q_val <= 0 or a_val <= 0:
            raise ValueError(f"Invalid {label} point '{item}'. Q and alpha must be > 0.")
        points.append((q_val, a_val))
    return points


def fit_alpha0_gamma(
    anchor_a: Tuple[float, float], anchor_b: Tuple[float, float], lambda_qcd: float
) -> Tuple[float, float]:
    q1, a1 = anchor_a
    q2, a2 = anchor_b
    gamma = math.log(a1 / a2) / math.log(q2 / q1)
    alpha0 = a1 / ((lambda_qcd / q1) ** gamma)
    return alpha0, gamma


def predict_alpha(alpha0: float, gamma: float, lambda_qcd: float, q_gev: float) -> float:
    return alpha0 * ((lambda_qcd / q_gev) ** gamma)


def weighted_rmse(residuals: Sequence[Tuple[float, float]]) -> float:
    # residual tuple: (residual, sigma)
    num = 0.0
    den = 0.0
    for resid, sigma in residuals:
        w = 1.0 / (sigma * sigma) if sigma > 0 else 1.0
        num += w * (resid * resid)
        den += w
    return math.sqrt(num / den) if den > 0 else float("nan")


def unweighted_rmse(values: Sequence[float]) -> float:
    if not values:
        return float("nan")
    return math.sqrt(sum(v * v for v in values) / len(values))


def linear_trend_slope(xs: Sequence[float], ys: Sequence[float]) -> float:
    if len(xs) != len(ys) or len(xs) < 2:
        return float("nan")
    x_mean = sum(xs) / len(xs)
    y_mean = sum(ys) / len(ys)
    num = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys))
    den = sum((x - x_mean) ** 2 for x in xs)
    return num / den if den != 0 else float("nan")


def format_report(
    lambda_qcd: float,
    anchor_a: Tuple[float, float],
    anchor_b: Tuple[float, float],
    alpha0: float,
    gamma: float,
    alpha0_nominal: float,
    gamma_nominal: float,
    holdout_data: Sequence[DataPoint],
) -> str:
    rows = []

    abs_residuals_fit = []
    rel_residuals_fit = []
    log_residuals_fit = []
    weighted_residuals_fit = []

    abs_residuals_nom = []
    rel_residuals_nom = []
    log_residuals_nom = []
    weighted_residuals_nom = []

    for dp in holdout_data:
        pred_fit = predict_alpha(alpha0, gamma, lambda_qcd, dp.q_gev)
        pred_nom = predict_alpha(alpha0_nominal, gamma_nominal, lambda_qcd, dp.q_gev)

        resid_fit = pred_fit - dp.alpha_obs
        rel_fit = resid_fit / dp.alpha_obs
        log_resid_fit = math.log(pred_fit / dp.alpha_obs)

        resid_nom = pred_nom - dp.alpha_obs
        rel_nom = resid_nom / dp.alpha_obs
        log_resid_nom = math.log(pred_nom / dp.alpha_obs)

        abs_residuals_fit.append(resid_fit)
        rel_residuals_fit.append(rel_fit)
        log_residuals_fit.append(log_resid_fit)
        weighted_residuals_fit.append((resid_fit, dp.sigma_obs))

        abs_residuals_nom.append(resid_nom)
        rel_residuals_nom.append(rel_nom)
        log_residuals_nom.append(log_resid_nom)
        weighted_residuals_nom.append((resid_nom, dp.sigma_obs))

        rows.append(
            "| {:.1f} | {:.6f} | {:.6f} | {:.6f} | {:+.6f} | {:+.3f}% | {:+.6f} | {:+.3f}% |".format(
                dp.q_gev,
                dp.alpha_obs,
                pred_fit,
                pred_nom,
                resid_fit,
                rel_fit * 100.0,
                resid_nom,
                rel_nom * 100.0,
            )
        )

    rmse_abs_fit = unweighted_rmse(abs_residuals_fit)
    rmse_rel_pct_fit = 100.0 * unweighted_rmse(rel_residuals_fit)
    rmse_log_fit = unweighted_rmse(log_residuals_fit)
    wrmse_abs_fit = weighted_rmse(weighted_residuals_fit)
    slope_rel_vs_logq_fit = linear_trend_slope(
        [math.log(dp.q_gev) for dp in holdout_data],
        rel_residuals_fit,
    )

    rmse_abs_nom = unweighted_rmse(abs_residuals_nom)
    rmse_rel_pct_nom = 100.0 * unweighted_rmse(rel_residuals_nom)
    rmse_log_nom = unweighted_rmse(log_residuals_nom)
    wrmse_abs_nom = weighted_rmse(weighted_residuals_nom)
    slope_rel_vs_logq_nom = linear_trend_slope(
        [math.log(dp.q_gev) for dp in holdout_data],
        rel_residuals_nom,
    )

    report_lines = [
        "## alpha_s Holdout Residual Report",
        "",
        "### Model Lock",
        "",
        "- Model: `alpha_s(Q) = alpha0 * (Lambda/Q)^gamma`",
        "- Lambda_QCD (GeV): `{:.6f}`".format(lambda_qcd),
        "- Anchor A1: `Q={:.3f} GeV, alpha_s={:.6f}`".format(anchor_a[0], anchor_a[1]),
        "- Anchor A2: `Q={:.3f} GeV, alpha_s={:.6f}`".format(anchor_b[0], anchor_b[1]),
        "- Fitted model alpha0: `{:.6f}`".format(alpha0),
        "- Fitted model gamma: `{:.6f}`".format(gamma),
        "- Nominal model alpha0: `{:.6f}`".format(alpha0_nominal),
        "- Nominal model gamma: `{:.6f}`".format(gamma_nominal),
        "",
        "### Holdout Results",
        "",
        "| Q (GeV) | alpha_obs | alpha_pred_fit | alpha_pred_nominal | resid_fit | rel_fit | resid_nominal | rel_nominal |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    report_lines.extend(rows)
    report_lines.extend(
        [
            "",
            "### Metrics (Fitted Model)",
            "",
            "- RMSE (absolute alpha_s): `{:.6f}`".format(rmse_abs_fit),
            "- RMSE (relative): `{:.3f}%`".format(rmse_rel_pct_fit),
            "- RMSE (log residual): `{:.6f}`".format(rmse_log_fit),
            "- Weighted RMSE (absolute): `{:.6f}`".format(wrmse_abs_fit),
            "- Residual trend slope vs log(Q): `{:+.6f}`".format(slope_rel_vs_logq_fit),
            "",
            "### Metrics (Nominal Model)",
            "",
            "- RMSE (absolute alpha_s): `{:.6f}`".format(rmse_abs_nom),
            "- RMSE (relative): `{:.3f}%`".format(rmse_rel_pct_nom),
            "- RMSE (log residual): `{:.6f}`".format(rmse_log_nom),
            "- Weighted RMSE (absolute): `{:.6f}`".format(wrmse_abs_nom),
            "- Residual trend slope vs log(Q): `{:+.6f}`".format(slope_rel_vs_logq_nom),
            "",
            "### Side-by-Side Comparison",
            "",
            "- Delta RMSE_abs (nominal - fitted): `{:+.6f}`".format(rmse_abs_nom - rmse_abs_fit),
            "- Delta RMSE_rel% (nominal - fitted): `{:+.3f}%`".format(rmse_rel_pct_nom - rmse_rel_pct_fit),
            "- Delta weighted RMSE (nominal - fitted): `{:+.6f}`".format(wrmse_abs_nom - wrmse_abs_fit),
            "- Delta trend slope (nominal - fitted): `{:+.6f}`".format(slope_rel_vs_logq_nom - slope_rel_vs_logq_fit),
            "",
            "Interpretation note:",
            "- Near-zero residual slope supports the bridge criterion of no scale-trending holdout residuals.",
            "- Lower RMSE and lower weighted RMSE indicate better holdout fit quality.",
            "- This report is fully determined by the model lock and selected A/P partition.",
            "",
        ]
    )

    return "\n".join(report_lines)


def build_default_holdout() -> Dict[float, DataPoint]:
    # Values from strong_coupling.md table (PDG-style benchmark list).
    return {
        2.0: DataPoint(2.0, 0.300, 0.020),
        5.0: DataPoint(5.0, 0.214, 0.005),
        10.0: DataPoint(10.0, 0.180, 0.004),
        34.0: DataPoint(34.0, 0.137, 0.003),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--lambda-qcd",
        type=float,
        default=0.2,
        help="Lambda_QCD in GeV (default: 0.2)",
    )
    parser.add_argument(
        "--anchors",
        nargs=2,
        default=["1.0:0.350", "91.2:0.1179"],
        metavar=("A1", "A2"),
        help="Two anchor points in Q:alpha format (default: 1.0:0.350 91.2:0.1179)",
    )
    parser.add_argument(
        "--holdout",
        nargs="*",
        default=["2.0:0.300", "5.0:0.214", "10.0:0.180", "34.0:0.137"],
        help="Holdout points in Q:alpha format",
    )
    parser.add_argument(
        "--out",
        default="",
        help="Optional output markdown file path; prints to stdout if omitted",
    )
    parser.add_argument(
        "--alpha0-nominal",
        type=float,
        default=0.35,
        help="Fixed nominal alpha0 for side-by-side comparison (default: 0.35)",
    )
    parser.add_argument(
        "--gamma-nominal",
        type=float,
        default=(3.0 / (4.0 * math.pi)),
        help="Fixed nominal gamma for side-by-side comparison (default: 3/(4*pi))",
    )

    args = parser.parse_args()

    anchor_points = parse_points(args.anchors, "anchor")
    holdout_points = parse_points(args.holdout, "holdout")

    holdout_defaults = build_default_holdout()
    holdout_data: List[DataPoint] = []
    for q_val, a_val in holdout_points:
        sigma = holdout_defaults.get(q_val, DataPoint(q_val, a_val, 0.01)).sigma_obs
        holdout_data.append(DataPoint(q_val, a_val, sigma))

    alpha0, gamma = fit_alpha0_gamma(anchor_points[0], anchor_points[1], args.lambda_qcd)

    report = format_report(
        lambda_qcd=args.lambda_qcd,
        anchor_a=anchor_points[0],
        anchor_b=anchor_points[1],
        alpha0=alpha0,
        gamma=gamma,
        alpha0_nominal=args.alpha0_nominal,
        gamma_nominal=args.gamma_nominal,
        holdout_data=holdout_data,
    )

    if args.out:
        with open(args.out, "w", encoding="utf-8") as handle:
            handle.write(report)
            if not report.endswith("\n"):
                handle.write("\n")
    else:
        print(report)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
