"""
This will import yahoo finance api to grab information and sort through 50
different stocks
"""
from yahoo_fin.stock_info import *
import pandas as pd
amazon = get_data('amzn', start_date='11/08/2020', end_date='11/08/2021', index_as_date=False, interval='1wk')
df = pd.DataFrame(amazon)
df.to_excel('Stocks.xlsx', sheet_name= 'Sheet1', na_rep='', float_format=.2, columns=None,)

class stocks():
    """
    Class stocks performs functions from the yahoo_fin package
    """
    
    # Annotate variables
    _ticker: str
    _price: float
 

    def __init__(self, ticker: str) -> None:
        """
        Initializes the parameters
        """
        self._ticker = ticker
        self._price = get_live_price(ticker)

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
        return self._price

    def get_open(self) -> list:
        """
        Returns the open data as a list
        """
        return self._data
    
    def get_close(self) -> list:
        """
        Returns the close data as a list
        """
        return self._data
    
    def get_high(self) -> list:
        """
        Returns the high data as a list
        """
        return self._data
    
    def get_low(self) -> list:
        """
        Returns the low data as a list
        """
        return self._data

    def get_adjclose(self) -> list:
        """
        Returns the adjclose data as a list
        """
        return self._data 

    def get_volume(self) -> list:
        """
        Returns the volume data as a list
        """
        return self._data 

   