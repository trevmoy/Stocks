"""
This will import yahoo finance api to grab information and sort through 50
different stocks
"""
from yahoo_fin.stock_info import *

class stocks():
    """
    Class stocks performs functions from the yahoo_fin package
    """
    
    # Annotate variables
    _ticker: str

    def __init__(self, ticker: str) -> None:
        """
        Initializes the parameters
        """
        self._ticker = ticker

    def __str__(self) -> str:
        """
        Returns a string version of the object
        """
        return f"{self._ticker}, {self._price}"

    def get_ticker(self) -> str:
        """
        Returns the ticker
        """
        return self._ticker
    
    def get_price(self) -> float:
        """
        Returns the price
        """
        price = get_live_price(self.get_ticker())
        return price

