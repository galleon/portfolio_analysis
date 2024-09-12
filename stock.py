from typing import Union

class Stock:
    """
    An instance of a stock holding consisting of name, shares, and price.
    """
    __slots__ = ('name', '_shares', 'price')

    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self) -> str:
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    @property
    def shares(self) -> int:
        return self._shares

    @shares.setter
    def shares(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Must be integer")
        self._shares = value

    @property
    def cost(self) -> float:
        """
        Return the cost as shares * price
        """
        return self.shares * self.price

    def sell(self, nshares: int) -> int:
        """
        Sell a number of shares and return the remaining number.
        """
        if nshares < 0:
            raise ValueError("Cannot sell a negative number of shares")
        if nshares > self.shares:
            raise ValueError("Cannot sell more shares than owned")
        self.shares -= nshares
        return self.shares
