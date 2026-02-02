# logscale

[![Actions Status][actions-badge]][actions-link]
[![Documentation Status][rtd-badge]][rtd-link]

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

[![GitHub Discussion][github-discussions-badge]][github-discussions-link]

[![Coverage][coverage-badge]][coverage-link]

This Python package provides a single function, `order_of_magnitude()`, which
computes and returns the order of magnitude of a given number in a standardized
string format.

The order of magnitude gives a compact representation of a number as a product
of a coefficient and a power of 10, where the coefficient is constrained to lie
within the interval [1/√10, √10). For more information, see the
[wikipedia article](https://en.wikipedia.org/wiki/Order_of_magnitude) on orders
of magnitude.

## Installation

If you are using `uv`, you can install the package from PyPI with:

    uv pip install logscale

Alternatively, with regular `pip`:

    pip install logscale

## Examples

```python
from logscale import order_of_magnitude

order_of_magnitude(129)  # "1.3e2"
order_of_magnitude(0.0001)  # "1.0e-4"
order_of_magnitude(456)  # "0.46e3"
order_of_magnitude(70.2)  # "0.70e2"
order_of_magnitude(0)  # "0.0e0"
```

<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/8-hat/logscale/workflows/CI/badge.svg
[actions-link]:             https://github.com/8-hat/logscale/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/logscale
[conda-link]:               https://github.com/conda-forge/logscale-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/8-hat/logscale/discussions
[pypi-link]:                https://pypi.org/project/logscale/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/logscale
[pypi-version]:             https://img.shields.io/pypi/v/logscale
[rtd-badge]:                https://readthedocs.org/projects/logscale/badge/?version=latest
[rtd-link]:                 https://logscale.readthedocs.io/en/latest/?badge=latest
[coverage-badge]:           https://codecov.io/github/8-hat/logscale/branch/main/graph/badge.svg
[coverage-link]:            https://codecov.io/github/8-hat/logscale

<!-- prettier-ignore-end -->
