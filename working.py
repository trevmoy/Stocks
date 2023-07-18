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

    # Indexing through the rows and columns to make modifications

    nasdaq: list = stocks.get_ticker()
    for row in range(1, len(nasdaq)):
        for col in range(1, 2):
            char = get_column_letter(col)
            ws[char + str(row)] = str(nasdaq[row])
                
    """for row in range(1, len(nasdaq)):
        for col in range(2, 3):
            char = get_column_letter(col)
            ws[char + str(row)] = str(stocks.get_price(nasdaq[row]))
            """

    # char +str(row)
    print("${:.2f}".format(stocks.get_price(nasdaq[1])))
    # Saves the document at the end of the code to update the actual excel sheet
    wb.save('Stocks.xlsx')

main()