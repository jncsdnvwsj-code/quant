# Pair Trading: Complete Mathematical and Practical Guide

A comprehensive Jupyter notebook on **pairs trading strategies** with rigorous mathematical foundations, statistical tests, and full implementation for KTH master's level mathematics students.

## Overview

Pair trading is a **market-neutral statistical arbitrage strategy** that exploits mean-reverting relationships between two correlated assets. This project provides:

✓ **Theoretical foundations** in cointegration and mean reversion  
✓ **Statistical testing methods** (Johansen, ADF, correlation analysis)  
✓ **Advanced modeling** (Ornstein-Uhlenbeck processes, Kalman filters)  
✓ **Complete backtesting framework** with performance metrics  
✓ **Risk management and position sizing** (Kelly criterion)  
✓ **Parameter optimization and sensitivity analysis**

## What's Inside

### 📚 13 Comprehensive Sections

1. **Data Loading & Libraries** - Historical price data setup for MSFT-AAPL pair
2. **Cointegration Theory** - Mathematical foundations (integration orders, Engle-Granger theorem)
3. **Statistical Arbitrage Fundamentals** - Mean reversion and trading mechanics
4. **Johansen Cointegration Test** - Eigenvalue analysis and pair selection
5. **Pairs Screening** - Hurst exponent, stationarity tests, screening algorithms
6. **Ornstein-Uhlenbeck Process** - Parameter estimation, half-life calculation, simulations
7. **Kalman Filter for Dynamic Hedging** - Time-varying hedge ratios
8. **Backtesting Framework** - Z-score signals, P&L tracking, performance metrics
9. **Risk Management & Position Sizing** - Kelly criterion, VaR, CVaR
10. **Parameter Optimization** - Sensitivity analysis and heatmaps
11. **Real-World Considerations** - Transaction costs, correlation stability
12. **Strategy Comparison** - 4 different strategies analyzed
13. **Summary & Takeaways** - Key formulas and implementation checklist

## Key Mathematical Concepts

### Cointegration
Two $I(1)$ processes with an $I(0)$ linear combination representing long-term equilibrium:
$$Z_t = \alpha X_t + \beta Y_t \sim I(0)$$

### Ornstein-Uhlenbeck Process
Mean-reverting dynamics with half-life:
$$dX_t = \theta(\mu - X_t)dt + \sigma dW_t$$
$$t_{1/2} = \frac{\ln(2)}{\theta}$$

### Z-Score Entry Signals
Trade when spread deviates significantly:
$$z_t = \frac{S_t - \mu}{\sigma}$$

### Kelly Criterion
Optimal position sizing for long-term growth:
$$f^* = \frac{bp - q}{b}$$

## Getting Started

### Requirements
- Python 3.8+
- Jupyter Notebook or JupyterLab
- Key packages:
  - `pandas` - Data manipulation
  - `numpy` - Numerical computing
  - `yfinance` - Stock data download
  - `scipy` - Statistical tests
  - `statsmodels` - Time series analysis
  - `scikit-learn` - Machine learning
  - `matplotlib`, `seaborn` - Visualization

### Installation

```bash
pip install numpy pandas matplotlib seaborn scipy yfinance statsmodels scikit-learn
```

### Running the Notebook

```bash
jupyter notebook Pair_Trading_Complete.ipynb
```

## Structure Overview

```
├── Section 1: Import & Data Loading
├── Section 2: Cointegration Theory (Math)
├── Section 3: Statistical Arbitrage (Theory)
├── Section 4: Johansen Test (Implementation)
├── Section 5: Pairs Screening (Algorithm)
├── Section 6: OU Process (Modeling)
├── Section 7: Kalman Filter (Advanced)
├── Section 8: Backtesting (Engine)
├── Section 9: Risk Management (Kelly, VaR)
├── Section 10: Parameter Optimization
├── Section 11: Transaction Costs
├── Section 12: Strategy Comparison
└── Section 13: Summary & Takeaways
```

## Example Analysis: MSFT-AAPL

The notebook uses Microsoft (MSFT) and Apple (AAPL) as the main example pair:

- **Data Period**: 2020-2024 (5 years, 1257 trading days)
- **Hedge Ratio**: 1.8082 (1 MSFT ≈ 1.81 AAPL)
- **R² Correlation**: 0.8652 (highly correlated)
- **Spread Mean**: 12.80
- **Spread Std Dev**: 29.88

## Key Findings

### Mean Reversion Characteristics
- ✓ Both price series are $I(1)$ (non-stationary)
- ✓ Their spread is $I(0)$ (stationary) → **cointegrated**
- ✓ Hurst exponent < 0.5 → **mean-reverting**

### Trading Performance (Example Strategy)
Different entry/exit thresholds produce varying results:
- **Conservative** (2.5σ/0.5σ): Lower frequency, higher quality
- **Moderate** (2.0σ/0.5σ): Balanced risk-return
- **Aggressive** (1.5σ/0.5σ): Higher frequency, lower win rate
- **Tight Exit** (2.0σ/0.2σ): Quick profit taking

## Main Components

### 1. Statistical Tests
```python
# ADF Test for stationarity
adfuller(series)

# Johansen Test for cointegration
coint_johansen(data)

# Engle-Granger cointegration
coint(series1, series2)
```

### 2. OU Parameter Estimation
```python
# Estimate θ (mean reversion speed)
# μ (long-term mean)
# σ (volatility)
ou_params = estimate_ou_parameters(spread)
```

### 3. Backtesting
```python
# Generate Z-score signals
# Calculate P&L and portfolio value
# Compute Sharpe ratio, max drawdown, win rate
backtester = PairTradingBacktester(X, Y, spread)
```

### 4. Position Sizing
```python
# Kelly criterion for optimal sizing
kelly_f, kelly_frac = kelly_criterion(win_rate, avg_win, avg_loss)

# Volatility-based sizing
position_size = volatility_adjusted_position_sizing(capital, target_vol, spread_vol)
```

## Customization

To analyze different pairs:

```python
main_pair = ('YOUR_TICKER1', 'YOUR_TICKER2')
price_data = load_pair_data(main_pair)
```

To change trading parameters:

```python
backtester = PairTradingBacktester(
    X, Y, spread,
    entry_threshold=2.0,    # Z-score entry level
    exit_threshold=0.5,     # Z-score exit level
    lookback=60,            # Rolling window (days)
    max_hold=20             # Maximum holding period
)
```

## Important Disclaimers

⚠️ **Educational Purpose Only**
- This code is for learning and research
- Backtests on historical data ≠ future performance
- Transaction costs and slippage significantly impact real returns
- Correlations break down during market crises

⚠️ **Risk Warnings**
- Pairs trading can experience extended drawdowns
- Liquidation risk if correlation breaks
- Model risk if assumptions are violated
- Requires proper risk management

## Further Learning Topics

Advanced areas to explore:
- Machine learning for pair selection
- Multi-leg arbitrage (3+ assets)
- Regime-switching models
- Cross-asset pairs (stocks, futures, options)
- Deep learning for price forecasting
- Portfolio-level pairs trading

## References

### Key Concepts
- **Engle, R. F., & Granger, C. W.** (1987) - Cointegration and error correction
- **Johansen, S.** (1991) - Likelihood-based inference for cointegration
- **Kalman, R. E.** (1960) - New approach to linear filtering
- **Kelly, J. L.** (1956) - A new interpretation of information rate

### Related Strategies
- Statistical arbitrage
- Convergence trading
- Relative value arbitrage
- Mean reversion strategies

## Contact & Usage

This project is part of KTH Master's Mathematics curriculum. Use responsibly and with proper risk management.

**Last Updated**: February 3, 2026

---

**Happy pair trading! 📈📊**
