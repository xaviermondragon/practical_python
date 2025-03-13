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
        next(rows) # skip headers
        for row in rows:
            try:
                no_shares = int(row[1])
                price = float(row[2])
                total_cost += no_shares * price
            except ValueError:
                print(f'Warning: The file {filename} has missing values at line: {row}')
        return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)