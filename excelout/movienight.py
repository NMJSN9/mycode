#!/usr/bin/python3
""" DOCSTRING """

import pandas as pd

def main():

    excel_file = 'movies.xls'

    movies = pd.read_excel(excel_file)
    print(movies.head()) #

                                             #first sheet
    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
    movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
    movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)

    movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])
    print(movies.shape)
   
    movies.drop_duplicates(inplace = True)
    
    sorted_by_gross = movies.sort_values(["Gross Earnings"], ascending=False)
    print(sorted_by_gross,movies.head(10))


main()

