# mathx/__init__.py
"""
Package initialization for mathx.stat distributions.


Import all distributions for ease of use:

>>> from mathx import PoissonDistribution, NegativeBinomialDistribution, Distribution



Wildcard import also supported:

>>> from mathx import *
    # imports Distribution, PoissonDistribution, NegativeBinomialDistribution



Allows importing directly from `mathx`:

>>> from mathx import PoissonDistribution, NegativeBinomialDistribution
>>> poisson = PoissonDistribution(lam=3.0)
>>> nb = NegativeBinomialDistribution(r=5, p=0.2)



Also supports:

>>> import mathx.stat as stat
>>> dist = stat.PoissonDistribution(lam=2.1)



"""
from .stat import *

__all__ = [
    'Distribution',
    'PoissonDistribution',
    'NegativeBinomialDistribution',
]
