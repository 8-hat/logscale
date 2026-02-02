from __future__ import annotations

import importlib.metadata

import logscale as m


def test_version():
    assert importlib.metadata.version("logscale") == m.__version__
