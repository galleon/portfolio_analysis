from stock import Stock
from typing import List, Dict, Union
from collections import Counter



class Portfolio:
    """
    A collection of stocks
    """
    def __init__(self, holdings: List[Stock]):
        self._holdings = holdings

    def __iter__(self):
        return iter(self._holdings)

    def __len__(self) -> int:
        return len(self._holdings)

    def __getitem__(self, index: int) -> Stock:
        return self._holdings[index]

    def __contains__(self, name: str) -> bool:
        return any(s.name == name for s in self._holdings)

    @property
    def total_cost(self) -> float:
        return sum(s.shares * s.price for s in self._holdings)

    def tabulate_shares(self) -> Counter[str]:
        total_shares: Counter[str]  = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
