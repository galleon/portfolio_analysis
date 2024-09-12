import argparse
from typing import Type

import report

class Portfolio:
    """
    A collection of stocks
    """
    def __init__(self, total_cost: float):
        self.total_cost = total_cost

def portfolio_cost(filename: str) -> float:
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    portfolio = report.read_portfolio(filename)  # Ensure this returns a Portfolio
    return portfolio.total_cost

def run() -> None:
    """
    Run the portfolio_cost function
    """
    parser = argparse.ArgumentParser(description="Compute the cost of a portfolio.")
    parser.add_argument("--portfolio", type=str, help="Path to the portfolio file.", default="data/portfolio.csv")
    args = parser.parse_args()

    filename = args.portfolio
    print('Total cost:', portfolio_cost(filename))

if __name__ == '__main__':
    """
    If the script is run from the command-line, parse the portfolio filename
    and print the total cost of the portfolio.
    """
    run()
