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

    # Adds titles to columns
    ws['A' + str(1)] = "Ticker"
    ws['B' + str(1)] = "Live Price"

    # Indexing through the rows and columns to make modifications
    nasdaq: list = stocks.get_ticker()
    for row in range(2, 21):
        ws['A' + str(row)] = str(nasdaq[row-1])
        ws['B' + str(row)] =  float("{:.2f}".format(stocks.get_price(nasdaq[row-1])))

            

    # Saves the document at the end of the code to update the actual excel sheet
    wb.save('Stocks.xlsx')

main()
