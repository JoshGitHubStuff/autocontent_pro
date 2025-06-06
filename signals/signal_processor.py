"""Signal processing and combination layer."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Dict, Any

from .llm_driver import LLMDriver


@dataclass
class SignalConfig:
    """Configuration for the signal processor."""

    include_unusual_options: bool = True
    include_iv_rank: bool = True


def mock_unusual_activity(ticker: str) -> float:
    """Mock unusual options activity metric."""
    return random.random()


def mock_iv_rank(ticker: str) -> float:
    """Mock implied volatility rank."""
    return random.random()


def mock_event_proximity(ticker: str) -> float:
    """Mock event proximity score."""
    return random.random()


class SignalProcessor:
    """Combines LLM output with market data for trading signals."""

    def __init__(self, llm: LLMDriver, config: SignalConfig | None = None) -> None:
        self.llm = llm
        self.config = config or SignalConfig()

    def fetch_signals(self, ticker: str) -> Dict[str, Any]:
        """Fetch and combine signals for a ticker."""
        texts = [f"Latest news and posts about {ticker}"]
        llm_output = self.llm.analyze(texts)
        signals: Dict[str, Any] = {
            "llm": llm_output,
            "unusual_activity": mock_unusual_activity(ticker) if self.config.include_unusual_options else None,
            "iv_rank": mock_iv_rank(ticker) if self.config.include_iv_rank else None,
            "event_proximity": mock_event_proximity(ticker),
        }
        return signals

