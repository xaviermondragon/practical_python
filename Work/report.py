# report.py
#
# Exercise 2.4

import csv
import sys

def read_portfolio(filename):
    """
        Read a stock portfolio file into a list of dictionaries with keys
        name, shares, and price.
    """
    portfolio = []
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        stock_keys = next(rows) # skip headers
        for row in rows:
            stock_vals = [row[0], int(row[1]), float(row[2])]
            stock = dict(zip(stock_keys, stock_vals))
            portfolio.append(stock)

    return portfolio

def read_prices(filename):
    """
        Read a CSV file of price data into a dict mapping names to prices.
    """
    prices =  {}
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print(f'Warning: The file {filename} has missing values.\n')

    return prices

def make_report(portfolio, prices):
    """
        Make a list of (name, shares, price, change) tuples given a portfolio list
        and prices dictionary.
    """
    rows=[]
    for stock in portfolio:
        name = stock['name']
        shares = stock['shares']
        actual_price = prices.get(name, 0)
        gain = actual_price - stock['price']
        rows.append((name, shares, actual_price, gain))
    return rows

if len(sys.argv) == 3:
    portfolio_filename = sys.argv[1]
    prices_filename = sys.argv[2]
else:
    portfolio_filename = 'Data/portfolio.csv'
    prices_filename = 'Data/prices.csv'

# Read data files and create the report data
portfolio = read_portfolio(portfolio_filename)
prices = read_prices(prices_filename)
report = make_report(portfolio, prices)

# Print a table showing info about the portfolio
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for row in report:
    #print('%10s %10d %10.2f %10.2f' % row)
    print('%10s %10d' % row[0:2], f'{f'${row[2]:.2f}':>10s}', f'{row[3]:>10.2f}')
