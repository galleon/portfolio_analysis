import argparse

from porty import Portfolio, Stock, create_formatter, parse_csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        portdicts = parse_csv(lines,
                              select=['name','shares','price'],
                              types=[str,int,float])

    portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
    return Portfolio(portfolio)

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as lines:
        return dict(parse_csv(lines, types=[str,float], has_headers=False))

def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for s in portfolio:
        current_price = prices[s.name]
        change = current_price - s.price
        summary = (s.name, s.shares, current_price, change)
        rows.append(summary)
    return rows

def print_report(reportdata, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = create_formatter(fmt)
    print_report(report, formatter)

def run():
    parser = argparse.ArgumentParser(description="Display a stock report.")
    parser.add_argument("--portfolio", type=str, help="Path to the portfolio file.", default="data/portfolio.csv")
    parser.add_argument("--prices", type=str, help="Path to the price file.", default="data/prices.csv")
    parser.add_argument("--format", type=str, help="Output format.", default="txt")
    args = parser.parse_args()

    portfolio_report(args.portfolio, args.prices, args.format)

if __name__ == '__main__':
    run()