Monte Carlo VaR
===============

This small project contains a Jupyter notebook that explains and implements Monte Carlo Value at Risk (VaR) and Expected Shortfall (ES) with clear mathematical derivations and runnable code.

Files:
- notebooks/Monte_Carlo_VaR.ipynb — the main explanatory notebook.
- monte_carlo_var.py — helper simulation functions.
- requirements.txt — recommended Python packages.

Quick start (Windows PowerShell):

1. Create and activate a virtual environment (optional but recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Start Jupyter and open the notebook:

```powershell
jupyter notebook
```

Notes:
- The notebook is self-contained and includes simulation examples (single asset and small portfolio), plots, and a bootstrap CI for VaR.
- Adjust Monte Carlo sample size `N` to trade off precision and compute time. For 99% VaR, use large `N` (e.g., 100k–1M) for stable estimates.

If you'd like, I can run the notebook here to validate outputs or add more examples (e.g., importance sampling or heavy-tailed models).