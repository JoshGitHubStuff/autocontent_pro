"""Core trading engine and utilities.

This module defines base classes for strategies, signal providers, and the
execution engine. It's intentionally lightweight so that additional
components can plug in easily.
"""

from dataclasses import dataclass
from typing import Protocol, Dict, Any


class SignalProvider(Protocol):
    """Interface for all signal providers."""

    def fetch_signals(self, ticker: str) -> Dict[str, Any]:
        """Return signal data for the given ticker."""


class Strategy(Protocol):
    """Interface for option trading strategies."""

    name: str

    def generate_trade(self, ticker: str, signals: Dict[str, Any]) -> Dict[str, Any]:
        """Return a trade recommendation based on signals."""


@dataclass
class TradeExecutionConfig:
    """Configuration for trade execution and risk controls."""

    paper: bool = True
    max_drawdown: float = 0.2
    trade_risk_pct: float = 0.05
    confidence_threshold: float = 0.5


class ExecutionEngine:
    """Simple execution engine for paper/live trading."""

    def __init__(self, config: TradeExecutionConfig) -> None:
        self.config = config

    def execute(self, trade: Dict[str, Any]) -> None:
        """Execute the trade. Placeholder for integration with brokers."""
        if self.config.paper:
            print(f"[PAPER] Executing trade: {trade}")
        else:
            print(f"[LIVE] Executing trade: {trade}")
            # Integration with Alpaca/IBKR would go here

