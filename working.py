"""
Testing the import openpyxl module
"""

# Imports from openpyxl and openpyxl.utils
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
from stocks import stocks
def main():
    # Accessing excel sheet using load_workbook
    wb = load_workbook('Stocks.xlsx')
    ws = wb.active

    # Asks the user to enter a ticker of a company
    ticker = input("Please enter a ticker for a company: ")
    price = stocks.get_price(ticker)

    # User object
    user = stocks(ticker)

    
    # Adds titles to columns
    ws['A' + str(1)] = "Ticker"
    ws['B' + str(1)] = "Live Price"

    # Indexing through the rows and columns to make modifications
    # nasdaq: list = stocks.get_ticker()
    for row in range(2, 3):
        ws['A' + str(row)] = str(user.get_ticker())
        ws['B' + str(row)] =  float("{:.2f}".format(price))

    # Saves the document at the end of the code to update the actual excel sheet
    wb.save('Stocks.xlsx')

main()
