# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import os
import argparse

def main(database: str, url_list_file:str ):
    print("We are going work with"+ database)
    print("We are going scan" + url_list_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-de", "--database", help="SQLite File Name")
    parser.add_argument("-i","--input",help="File containing urls to read")
    args = parser.parse_args()
    database_file = args.database
    input_file = args.inpu
    main(database=database_file,url_list_file=input_file)