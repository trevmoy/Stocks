"""
Testing the import openpyxl module
"""

# Imports from openpyxl and openpyxl.utils
from stocks import stocks
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import *
from pandas import *

def main():
    """
    In main the input and function calls occur
    """

    # Assigns the workbook and worksheet to variables wb and ws
    wb = load_workbook('NewStocks.xlsx')
    ws = wb.active

    # Deletes any pre-existing content in the sheet
    ws.delete_rows(1, ws.max_row)

    # Asks the user to enter a ticker, start date, end date, and 
    ticker = input("Please enter a ticker for a company: ")
    startDate = input("Please enter a start date(ex: 12/06/2005): ")
    endDate = input("Please enter an end date(ex: 12/06/2005): ")
    interval = input("Please enter the interval you'd like(ex: 1d, 1wk, 1mo): ")

    # Instantiates the stocks object, passing the input through the parameters and assigning it as 'user'
    # Object instantiation is placed in a try-except handler to catch invalid input
    try:
        user = stocks(ticker, startDate, endDate, interval)
    except:
        # Asks user to re-enter valid input
        print("Please enter valid input.")
        ticker = input("Please enter a ticker for a company: ")
        startDate = input("Please enter a start date(ex: 12/06/2005): ")
        endDate = input("Please enter an end date(ex: 12/06/2005): ")
        interval = input("Please enter the interval you'd like(ex: 1d, 1wk, 1mo): ")

        user = stocks(ticker, startDate, endDate, interval)


    # Sorts through df retrieved from the stocks class, sets index & header equal to true and appends each cell with the df info
    for r in dataframe_to_rows(user.get_info(), index=True, header=True, ):
        ws.append(r)

    # Sets the index and header style to the default pandas style
    for cell in ws['A'] + ws[1]:
        cell.style = 'Pandas'

    # Correcting unnecessary columns and rows
    ws.delete_cols(1,1)
    ws.delete_rows(2,2)

    # Saves the document at the end of the code to update the actual excel sheet
    wb.save('NewStocks.xlsx')

    # Print statement to let users know that the spreadsheet is ready for viewing
    print("Your new excel sheet is ready!")
main()
