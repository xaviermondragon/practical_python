# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    """
        Computes the total cost (shares*price) of a portfolio file
    """

    total_cost = 0.0
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows) # skip headers
        for row_no, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                no_shares = int(record['shares'])
                price = float(record['price'])
                total_cost += no_shares * price
            except ValueError:
                print(f'Warning: Couldn\'t convert row number {row_no}: {row}')
        return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    #filename = 'Data/portfolio.csv'
    filename = input('Enter a portfolio filename: ')

cost = portfolio_cost(filename)
print('Total cost:', cost)