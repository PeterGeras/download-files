import sys
import os
from os import listdir
from os.path import isfile, join
from pandas import *


# Current working directory
cwd = os.getcwd()

xls_path = cwd + r'\input\URL_short.xlsx'


def parse_excel():
    xls = ExcelFile(xls_path)
    data = pandas.read_excel(xls).to_dict('record')

    for row in data:
        print(f'{row}')
        print(f'Name = {row["Name"]}, URL = {row["Url"]}')


def main():
    parse_excel()
    
    return True


if __name__ == '__main__':
    main()

