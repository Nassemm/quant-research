# Quant Research Portfolio

This repository contains quantitative finance research projects implemented in Python.

## Project 1: ETF Momentum Strategy

Universe:
SPY, QQQ, IWM, TLT, GLD

Strategy rules:
- Calculate 3-month momentum
- Require price above 100-day moving average
- Hold top 2 ETFs
- Equal weight portfolio

Performance (2010–present):
- CAGR ≈ 11.7%
- Sharpe Ratio ≈ 0.86
- Max Drawdown ≈ −26%

Tools used:
Python, pandas, numpy, matplotlib, yfinance, Jupyter