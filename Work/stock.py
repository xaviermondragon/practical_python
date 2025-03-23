# stock.py

class Stock:
    """
        An instance of a stock holding consisting of name, shares, and price.
    """
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'

    def cost(self):
        """
            Return the price of the portfolio
        """
        return self.shares * self.price

    def sell(self, no_shares):
        """
            Sell a number of shares
        """
        self.shares -= no_shares
