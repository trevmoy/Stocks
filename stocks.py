"""
This will import yahoo finance api to grab information and sort through 50
different stocks
"""
from yahoo_fin.stock_info import *

class stocks():
    """
    class stocks
    """

    def get_ticker() -> list:
        """
        Pulls tickers from nasdaq and indexes through every one in the list
        """
        tickers = tickers_nasdaq()
        tickers_nasdaq(True)
        return tickers
    
    def get_price(ticker: str) -> float:
        return get_live_price(ticker)

