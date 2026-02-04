Spectral filtering of financial correlation matrices

This repository contains a Jupyter notebook demonstrating spectral filtering of financial correlation matrices using Random Matrix Theory (RMT) and comparisons to Ledoit–Wolf shrinkage.

Files:
- notebooks/spectral_filtering.ipynb - main notebook with theory, code, and a simple backtest.
- requirements.txt - Python dependencies.

Quick start:
1. Create a virtual environment and install dependencies:

```bash
python -m venv venv
# Windows PowerShell
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Launch Jupyter Lab / Notebook and open the notebook:

```bash
jupyter lab
# or
jupyter notebook
```

Notes:
- The notebook uses `yfinance` to download price data; internet access is required.
- The code is educational and suitable for experimentation; adapt ticker lists, windows, and methods as needed.
