import stock
import pytest
import os

def test_create():
    s = stock.Stock('GOOG', 100, 490.1)
    assert s.name == 'GOOG'
    assert s.shares == 100
    assert s.price == 490.1

def test_cost():
  s = stock.Stock('GOOG', 100, 490.1)
  assert s.cost == 49010.0

def test_sell():
    s = stock.Stock('GOOG', 100, 490.1)
    s.sell(25)
    assert s.shares == 75

def test_shares_check():
    s = stock.Stock('GOOG', 100, 490.1)
    with pytest.raises(TypeError):
        s.shares = '100'

