"""logscale package initialization module."""

from __future__ import annotations

from ._version import version as __version__
from .order_of_magnitude import order_of_magnitude

__all__ = ["__version__", "order_of_magnitude"]
