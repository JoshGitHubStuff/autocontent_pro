"""Command line interface for the trading bot."""

from __future__ import annotations

import argparse
from typing import Dict, Any

from core.engine import ExecutionEngine, TradeExecutionConfig
from signals.llm_driver import LLMDriver
from signals.signal_processor import SignalProcessor
from strategies.earnings_momentum import EarningsMomentumStrategy


STRATEGY_MAP = {
    "earnings_momentum": EarningsMomentumStrategy(),
}


def run_signal_scan(ticker: str) -> None:
    """Run sentiment and volatility scan for a ticker."""
    llm = LLMDriver()
    processor = SignalProcessor(llm)
    signals = processor.fetch_signals(ticker)
    print(signals)


def run_strategy(name: str, ticker: str, paper: bool) -> None:
    """Execute a strategy."""
    strategy = STRATEGY_MAP.get(name)
    if not strategy:
        raise ValueError(f"Unknown strategy: {name}")
    llm = LLMDriver()
    processor = SignalProcessor(llm)
    signals = processor.fetch_signals(ticker)
    trade = strategy.generate_trade(ticker, signals)
    engine = ExecutionEngine(TradeExecutionConfig(paper=paper))
    engine.execute(trade)


def evaluate(ticker: str) -> None:
    """Placeholder backtest/evaluation command."""
    print(f"Running backtest for {ticker} ...")


def main(args: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Options trading bot")
    sub = parser.add_subparsers(dest="cmd", required=True)

    scan_parser = sub.add_parser("run_signal_scan")
    scan_parser.add_argument("ticker")

    strat_parser = sub.add_parser("run_strategy")
    strat_parser.add_argument("strategy_name")
    strat_parser.add_argument("ticker")
    strat_parser.add_argument("--paper", action="store_true", default=False)

    eval_parser = sub.add_parser("evaluate")
    eval_parser.add_argument("ticker")

    parsed = parser.parse_args(args)

    if parsed.cmd == "run_signal_scan":
        run_signal_scan(parsed.ticker)
    elif parsed.cmd == "run_strategy":
        run_strategy(parsed.strategy_name, parsed.ticker, parsed.paper)
    elif parsed.cmd == "evaluate":
        evaluate(parsed.ticker)


if __name__ == "__main__":
    main()

