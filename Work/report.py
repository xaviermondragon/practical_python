# report.py

import fileparse
from stock import Stock
from portfolio import Portfolio
import tableformat

def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of stock objects, each with
    name, shares, and price fields
    """
    with open(filename) as file:
        port_dicts = fileparse.parse_csv(file, select=['name','shares','price'], types=[str,int,float])
    portfolio = [Stock(d['name'], d['shares'], d['price']) for d in port_dicts]
    return Portfolio(portfolio)

def read_prices(filename):
    """
    Read a CSV file of price data into a dict mapping names to prices.
    """
    with open(filename) as file:
        return dict(fileparse.parse_csv(file, types=[str,float], has_headers=False))

def make_report(portfolio, prices):
    """
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    """
    rows=[]
    for stock in portfolio:
        name = stock.name
        shares = stock.shares
        actual_price = prices.get(name, 0)
        gain = actual_price - stock.price
        rows.append((name, shares, actual_price, gain))
    return rows

def print_report(report_data, formatter):
    """
    Print a nicely formated table from a list of (name, shares, price, change)
    """
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report_data:
        row_data = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(row_data)

    # headers = ('Name', 'Shares', 'Price', 'Change')
    # print('%10s %10s %10s %10s' % headers)
    # print(('-' * 10 + ' ') * len(headers))
    # for row in report_data:
    #     # print('%10s %10d %10.2f %10.2f' % row)
    #     print('%10s %10d' % row[0:2], f'{f'${row[2]:.2f}':>10s}', f'{row[3]:>10.2f}')

def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    """
    Make a stock report given portfolio and price data files.
    """
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Create the report data
    report_data = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report_data, formatter)

def main(argv):
    if len(argv) != 4:
        raise SystemExit('Usage: %s portfile pricefile format' % argv[0])
    portfolio_report(argv[1], argv[2], argv[3])


if __name__ == '__main__':
    import sys
    main(sys.argv)
