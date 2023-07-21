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

    # Asks the user to enter a ticker of a company and instantiates an object called user
    ticker = input("Please enter a ticker for a company: ")
    startDate = input("Please enter a start date(ex: 12/06/2005): ")
    endDate = input("Please enter an end date(ex: 12/06/2005): ")
    interval = input("Please enter the interval you'd like(ex: 1d, 1wk, 1mo): ")
    user = stocks(ticker, startDate, endDate, interval)
    # Assigns price the value of the current strock price by calling get_price method through the user object
    user.get_info()
    """price = user.get_price()

    # Adds titles to columns
    ws['A' + str(1)] = "Ticker"
    ws['B' + str(1)] = "Live Price"
    
    # Modifies the cells to display information and tidy up the appearance
    for i in range(2, 3):
        for row in range(2, 3):
            for col in range(1, i):
                char = get_column_letter(col)
                ws[char + str(row)] = str(user.get_ticker().upper())
            for col in range(i, i+1):
                char = get_column_letter(col)
                ws[char + str(row)] = float("{:.2f}".format(price))
    # Saves the document at the end of the code to update the actual excel sheet 
    wb.save('Stocks.xlsx')"""

main()
