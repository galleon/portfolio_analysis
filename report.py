from typing import Any, List, Dict, Iterable, Tuple
from stock import Stock
import fileparse
from tableformat import TableFormatter, createFormatter
from portfolio import Portfolio
import argparse


def read_portfolio(filename: str) -> Portfolio:
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    with open(filename) as lines:
        portdicts: Any = fileparse.parse_csv(
            lines,
            select=['name', 'shares', 'price'],
            types=[str, int, float]
        )

    portfolio: List[Stock] = [Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    return Portfolio(portfolio)


def read_prices(filename: str) -> Dict[str, float]:
    """
    Read a CSV file of price data into a dict mapping names to prices.
    """
    with open(filename) as lines:
        prices_list: Any = fileparse.parse_csv(
            lines,
            types=[str, float],
            has_headers=False
        )
    return dict(prices_list)


def make_report_data(portfolio: Portfolio, prices: Dict[str, float]) -> List[Tuple[str, int, float, float]]:
    """
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    """
    rows: List[Tuple[str, int, float, float]] = []
    for s in portfolio:
        current_price = prices.get(s.name, 0.0)  # Use .get() to avoid KeyError
        change = current_price - s.price
        summary = (s.name, s.shares, current_price, change)
        rows.append(summary)
    return rows


def print_report(reportdata: List[Tuple[str, int, float, float]], formatter: TableFormatter) -> None:
    """
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    """
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfoliofile: str, pricefile: str, fmt: str = 'txt') -> None:
    """
    Make a stock report given portfolio and price data files.
    """
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = createFormatter(fmt)
    print_report(report, formatter)


def run() -> None:
    """
    Run the portfolio_report function
    """
    parser = argparse.ArgumentParser(description="Display a stock report.")
    parser.add_argument("--portfolio", type=str, help="Path to the portfolio file.", default="data/portfolio.csv")
    parser.add_argument("--prices", type=str, help="Path to the price file.", default="data/prices.csv")
    parser.add_argument("--format", type=str, help="Output format.", default="txt")
    args = parser.parse_args()

    portfolio_report(args.portfolio, args.prices, args.format)


if __name__ == '__main__':
    """
    If the script is run from the command-line, parse the portfolio and price
    filenames and print the stock report.
    """
    run()
