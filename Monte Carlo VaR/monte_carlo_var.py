import numpy as np

def simulate_gbm_returns(S0, mu, sigma, dt, n_scenarios):
    """Simulate GBM one-step log-returns and P&L."""
    drift = (mu - 0.5 * sigma ** 2) * dt
    vol = sigma * np.sqrt(dt)
    Z = np.random.normal(size=n_scenarios)
    logR = drift + vol * Z
    S1 = S0 * np.exp(logR)
    pnl = S1 - S0
    return pnl, logR


def empirical_var(losses, alpha=0.95):
    losses = np.asarray(losses)
    return np.quantile(losses, alpha)


def empirical_es(losses, alpha=0.95):
    losses = np.asarray(losses)
    q = empirical_var(losses, alpha)
    tail = losses[losses >= q]
    if len(tail) == 0:
        return q
    return tail.mean()


def simulate_portfolio_losses(weights, S0s, mus, sigmas, corr, dt, N):
    n = len(S0s)
    cov = np.outer(sigmas, sigmas) * corr * dt
    mean = (mus - 0.5 * sigmas**2) * dt
    L = np.linalg.cholesky(cov)
    Z = np.random.normal(size=(N, n))
    correlated = Z @ L.T + mean
    S1 = S0s * np.exp(correlated)
    pnls = (S1 - S0s) * weights
    portfolio_pnl = pnls.sum(axis=1)
    losses = -portfolio_pnl
    return losses


def bootstrap_var_ci(losses, alpha=0.99, B=1000, ci=0.95):
    n = len(losses)
    var_boot = np.empty(B)
    for b in range(B):
        sample = np.random.choice(losses, size=n, replace=True)
        var_boot[b] = np.quantile(sample, alpha)
    lower = np.quantile(var_boot, (1-ci)/2)
    upper = np.quantile(var_boot, 1-(1-ci)/2)
    return (lower, upper), var_boot
