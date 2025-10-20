from __future__ import annotations
import argparse
import os
import numpy as np

#!/usr/bin/env python3
"""
Simple data-science demo:
- generates a synthetic dataset (x, y)
- fits a linear regression (OLS) using numpy
- prints metrics and saves data and an optional plot
Save this file as main.py and run: python main.py
"""


def highlight(text: str) -> str:    
    return f"\033[1;32m{text}\033[0m"

def generate_data(n: int = 100, seed: int | None = 0):
    rng = np.random.default_rng(seed)
    x = rng.uniform(-10, 10, size=n)
    noise = rng.normal(loc=0.0, scale=5.0, size=n)
    y = 3.5 * x + 1.2 + noise
    return x, y

def fit_linear_regression(x: np.ndarray, y: np.ndarray):
    # Design matrix with intercept
    A = np.column_stack((np.ones_like(x), x))
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    intercept, slope = coef[0], coef[1]
    y_pred = intercept + slope * x
    mse = float(np.mean((y - y_pred) ** 2))
    ss_res = float(np.sum((y - y_pred) ** 2))
    ss_tot = float(np.sum((y - y.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot != 0 else float("nan")
    return {"intercept": intercept, "slope": slope, "mse": mse, "r2": r2, "y_pred": y_pred}

def save_csv(path: str, x: np.ndarray, y: np.ndarray):
    header = "x,y"
    data = np.column_stack((x, y))
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    np.savetxt(path, data, delimiter=",", header=header, comments="")

def try_plot(x: np.ndarray, y: np.ndarray, y_pred: np.ndarray, out_path: str = "plot.png"):
    try:
        import matplotlib.pyplot as plt
    except Exception:
        return False
    plt.figure(figsize=(6, 4))
    plt.scatter(x, y, label="data", alpha=0.6)
    order = np.argsort(x)
    plt.plot(x[order], y_pred[order], color="C1", label="fit", linewidth=2)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()
    return True

def main():
    p = argparse.ArgumentParser(description="Generate synthetic data and fit a linear model.")
    p.add_argument("--n", type=int, default=100, help="number of samples")
    p.add_argument("--seed", type=int, default=0, help="random seed")
    p.add_argument("--out", type=str, default="data.csv", help="CSV output path")
    args = p.parse_args()

    x, y = generate_data(n=args.n, seed=args.seed)
    result = fit_linear_regression(x, y)

    save_csv(args.out, x, y)

    print(f"Saved data to: {args.out}")
    print(f"Intercept: {result['intercept']:.4f}")
    print(f"Slope    : {result['slope']:.4f}")
    print(f"MSE      : {result['mse']:.4f}")
    print(f"R^2      : {result['r2']:.4f}")

    plotted = try_plot(x, y, result["y_pred"], out_path="plot.png")
    if plotted:
        print("Saved plot to: plot.png")
    else:
        print("matplotlib not available; skipping plot.")

if __name__ == "__main__":
    main()