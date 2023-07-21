"""
Testing the import openpyxl module
"""

# Imports from openpyxl and openpyxl.utils
from stocks import stocks
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import *
from pandas import *

def main():
    
    # Accessing excel sheet using load_workbook
    wb = load_workbook('NewStocks.xlsx')
    ws = wb.active

    # Asks the user to enter a ticker of a company and instantiates an object called user
    ticker = input("Please enter a ticker for a company: ")
    startDate = input("Please enter a start date(ex: 12/06/2005): ")
    endDate = input("Please enter an end date(ex: 12/06/2005): ")
    interval = input("Please enter the interval you'd like(ex: 1d, 1wk, 1mo): ")

    user = stocks(ticker, startDate, endDate, interval)

    # Assigns price the value of the current strock price by calling get_price method through the user object
    for r in dataframe_to_rows(user.get_info(), index=True, header=True, ):
        ws.append(r)


    print("Your new excel sheet is ready!")


    for cell in ws['A'] + ws[1]:
        cell.style = 'Pandas'


    ws.delete_cols(1,1)
    ws.delete_rows(2,2)

    # Saves the document at the end of the code to update the actual excel sheet
    wb.save('NewStocks.xlsx')

main()
