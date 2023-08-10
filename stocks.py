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

    def get_info(self) -> pd:
        """
        Returns the dataframe info of the stock
        Uses a try-except-else to handle errors. 
        If an error is encountered, the exception will return false to the main function.
        The else will create a pandas dataframe and return it to the main function.
        """
        try:
            stock = get_data(self._ticker, 
                                start_date=self._startDate, 
                                end_date=self._endDate, 
                                index_as_date=True, 
                                interval=self._interval)
        except:
            return False
        else:
            df = pd.DataFrame(stock)
            df.index.names = ['date']
            df.reset_index(level=0, inplace=True)
            return df

    def get_nasdaq() -> list:
        """
        Prints all the available tickers listed on the nasdaq
        """
        return tickers_nasdaq()
    
    def get_line_graph():
        """
        Returns a line plot to see the different flucuations over time.
        """
    pd.plotting