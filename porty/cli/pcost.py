import argparse

from porty.cli.report import read_portfolio

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = read_portfolio(filename)
    return portfolio.total_cost

def run():
    parser = argparse.ArgumentParser(description="Compute the cost of a portfolio.")
    parser.add_argument("--portfolio", type=str, help="Path to the portfolio file.", default="data/portfolio.csv")
    args = parser.parse_args()

    filename = args.portfolio
    print('Total cost:', portfolio_cost(filename))

if __name__ == '__main__':
    run()
