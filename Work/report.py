# report.py
#
# Exercise 2.4

import csv
import sys
import fileparse

def read_portfolio(filename):
    """
        Read a stock portfolio file into a list of dictionaries with keys
        name, shares, and price.
    """
    return fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])


def read_prices(filename):
    """
        Read a CSV file of price data into a dict mapping names to prices.
    """
    return dict(fileparse.parse_csv(filename, types=[str,float], has_headers=False))


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


def print_report(report):
    """
        Print a nicely formated table from a list of (name, shares, price, change)
    """
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        # print('%10s %10d %10.2f %10.2f' % row)
        print('%10s %10d' % row[0:2], f'{f'${row[2]:.2f}':>10s}', f'{row[3]:>10.2f}')

def portfolio_report(portfolio_filename, prices_filename):
    """
        Make a stock report given portfolio and price data files.
    """
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

if len(sys.argv) == 3:
    portfolio_filename = sys.argv[1]
    prices_filename = sys.argv[2]
else:
    portfolio_filename = 'Data/portfolio.csv'
    prices_filename = 'Data/prices.csv'
    #portfolio_filename = input('Enter portfolio filename: ')
    #prices_filename = input('Enter prices filename: ')

portfolio_report(portfolio_filename, prices_filename)




