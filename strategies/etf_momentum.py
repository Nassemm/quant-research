import yfinance as yf
import pandas as pd
import numpy as np

tickers = ["SPY","QQQ","IWM","TLT","GLD"]

def run_strategy():

    data = yf.download(
        tickers,
        start="2010-01-01",
        auto_adjust=True,
        progress=False,
        threads=False
    )["Close"]

    returns = data.pct_change()
    momentum = data.pct_change(63)
    ma100 = data.rolling(100).mean()

    trend_filter = data > ma100
    ranks = momentum.rank(axis=1, ascending=False)

    top2 = ranks <= 2
    signals = top2 & trend_filter

    weights = signals.shift(1).astype(float)
    weights = weights.div(weights.sum(axis=1), axis=0).fillna(0)

    strategy_returns = (weights * returns).sum(axis=1)

    equity = (1 + strategy_returns.fillna(0)).cumprod()

    sharpe = strategy_returns.mean() / strategy_returns.std() * np.sqrt(252)

    cummax = equity.cummax()
    drawdown = (equity - cummax) / cummax
    max_drawdown = drawdown.min()

    cagr = equity.iloc[-1] ** (252 / len(equity)) - 1

    print("Sharpe:", round(sharpe,2))
    print("Max Drawdown:", round(max_drawdown,2))
    print("CAGR:", round(cagr,2))

    return equity


if __name__ == "__main__":
    run_strategy()