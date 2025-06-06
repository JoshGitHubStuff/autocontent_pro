# autocontent_pro

This project provides a modular Python framework for generating option
trading signals using large language models (LLMs). It includes a simple
CLI for running scans, executing strategies, and evaluating trades.

```
core/       # base engine and execution layer
signals/    # LLM-driven sentiment analysis and signal combination
strategies/ # pluggable trading strategies
cli/        # command line interface entry point
```

The example implementation contains a placeholder LLM driver and a basic
`earnings_momentum` strategy. These components can be extended with real
API calls and additional strategies.

