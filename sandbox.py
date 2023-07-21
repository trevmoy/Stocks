"""
This is a sandbox enviornment for testing new features
"""
from yahoo_fin.stock_info import *
import pandas as pd
amazon = get_data('amzn', start_date='11/08/2020', end_date='11/08/2021', index_as_date=False, interval='1wk')
df = pd.DataFrame(amazon)
df.to_excel('Stocks.xlsx', 
            sheet_name= 'Sheet1', 
            na_rep='', 
            float_format="%.2f", 
            columns=None, 
            header=True, 
            index=False, 
            inf_rep='inf',
            freeze_panes=None)