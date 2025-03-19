# pcost.py
#
# Exercise 1.27

import sys
import report

def portfolio_cost(filename):
    """
        Computes the total cost (shares*price) of a portfolio file
    """
    portfolio = report.read_portfolio(filename)
    return sum([stock['shares'] * stock['price'] for stock in portfolio])

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a portfolio filename: ')

cost = portfolio_cost(filename)
print('Total cost:', cost)