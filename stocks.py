"""
This will import yahoo finance api to grab information and sort through 50
different stocks
"""
from yahoo_fin.stock_info import *
import pandas as pd


class stocks():
    """
    Class stocks performs functions from the yahoo_fin package
    """
    
    # Annotate variables
    _ticker: str
    _price: float
    _startDate: str
    _endDate: str
    _interval: str
 

    def __init__(self, ticker: str, startDate: str, endDate: str, interval: str) -> None:
        """
        Initializes the parameters
        """
        self._ticker = ticker
        self._price = get_live_price(ticker)
        self._startDate = startDate
        self._endDate = endDate
        self._interval = interval

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

    def get_info(self):
        """
        Returns the csv conversion
        """
        stock = get_data(self._ticker, 
                         start_date=self._startDate, 
                         end_date=self._endDate, 
                         index_as_date=False, 
                         interval=self._interval)
        df = pd.DataFrame(stock)
        df.to_excel('Stocks.xlsx', 
            sheet_name= 'Sheet1', 
            na_rep='', 
            float_format="%.2f", 
            columns=None, 
            header=True, 
            index=False, 
            inf_rep='inf',
            freeze_panes=None)
        return None
