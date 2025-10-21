import math
from abc import ABC, abstractmethod

class Distribution(ABC):
    """
    Abstract base class for discrete probability distributions.

    Subclasses must implement the `pmf(k)` method, and get
    `distribution` and `reversed_distribution` for free.
    """
    @abstractmethod
    def pmf(self, k: int) -> float:
        """
        Probability mass function: P(X = k).

        Args:
            k (int): Non-negative integer event count.

        Returns:
            float: Probability that the random variable equals k.
        """
        pass

    def distribution(self, max_k: int) -> list[float]:
        """
        Full PMF from 0 to max_k.

        Args:
            max_k (int): Maximum count (>= 0)

        Returns:
            list[float]: [P(X=0), ..., P(X=max_k)]
        """
        if max_k < 0 or not isinstance(max_k, int):
            raise ValueError("max_k must be a non-negative integer.")
        return [self.pmf(i) for i in range(max_k + 1)]

    def reversed_distribution(self, max_k: int) -> list[float]:
        """
        PMF in reverse order: P(X=max_k) down to P(X=0).

        Args:
            max_k (int): Maximum count (>= 0)

        Returns:
            list[float]: [P(X=max_k), ..., P(X=0)]
        """
        return self.distribution(max_k)[::-1]


class PoissonDistribution(Distribution):
    """
    Poisson distribution with average rate λ.
    """
    def __init__(self, lam: float):
        if lam <= 0:
            raise ValueError("Lambda must be a positive number.")
        self.lam = lam

    def pmf(self, k: int) -> float:
        if k < 0 or not isinstance(k, int):
            raise ValueError("k must be a non-negative integer.")
        return (self.lam ** k) * math.exp(-self.lam) / math.factorial(k)


class NegativeBinomialDistribution(Distribution):
    """
    Negative Binomial distribution (counting number of failures before `r` successes).

    PMF: P(X = k) = C(k + r - 1, k) * (1 - p)^k * p^r
    where
      - r: number of successes (positive integer)
      - p: probability of success on each trial (0 < p <= 1)
      - k: number of failures (>= 0)
    """
    def __init__(self, r: int, p: float):
        if r <= 0 or not isinstance(r, int):
            raise ValueError("r (number of successes) must be a positive integer.")
        if not (0 < p <= 1):
            raise ValueError("p (success probability) must be in the interval (0, 1].")
        self.r = r
        self.p = p

    def pmf(self, k: int) -> float:
        if k < 0 or not isinstance(k, int):
            raise ValueError("k (failures) must be a non-negative integer.")
        # Combination: (k+r-1 choose k)
        comb = math.comb(k + self.r - 1, k)
        return comb * ((1 - self.p) ** k) * (self.p ** self.r)













if __name__ == "__main__":
    # Example usage for PoissonDistribution
    poisson = PoissonDistribution(lam=4.5)
    max_k = 10
    print(poisson.distribution(max_k))
    print(poisson.reversed_distribution(max_k))



    

    print(f"Poisson distribution for λ = {poisson.lam} from 0 to {max_k}:")
    for i, p in enumerate(poisson.distribution(max_k)):
        print(f"P(X={i}) = {p:.6f}")

    print("\nReversed:")
    for idx, p in enumerate(poisson.reversed_distribution(max_k)):
        k = max_k - idx
        print(f"P(X={k}) = {p:.6f}")








    # Example usage for NegativeBinomialDistribution
    negbin = NegativeBinomialDistribution(r=3, p=0.4)
    max_k_nb = 10
    print(negbin.distribution(max_k_nb))
    print(negbin.reversed_distribution(max_k_nb))




    print(f"\nNegative Binomial distribution for r = {negbin.r}, p = {negbin.p} (failures 0 to {max_k_nb}):")
    for k, p in enumerate(negbin.distribution(max_k_nb)):
        print(f"P(X={k} failures) = {p:.6f}")

    print("\nReversed NB:")
    for idx, p in enumerate(negbin.reversed_distribution(max_k_nb)):
        k = max_k_nb - idx
        print(f"P(X={k} failures) = {p:.6f}")
