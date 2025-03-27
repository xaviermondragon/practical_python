# pcost.py

import report

def portfolio_cost(filename):
    """
        Computes the total cost (shares*price) of a portfolio file
    """
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost

def main(argv):
    if len(sys.argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} portfolio_filename')
    cost = portfolio_cost(argv[1])
    print('Total cost:', cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)
