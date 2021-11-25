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
from uttilities import url_uttilities


def main(database: str, url_list_file: str) :
    big_word_list = []
    print("We are going work with" + database)
    print("We are going scan " + url_list_file)
    urls = url_uttilities.load_urls_from_file(url_list_file)
    for url in urls:
        print("Reading " + url)
        page_content = url_uttilities.load_page(url=url)
        # print ( page_content)
        words = url_uttilities.scrape_page(page_contents=page_content)
        big_word_list.extend(words)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-de", "--database", help="SQLite File Name")
    parser.add_argument("-i", "--input", help="File containing urls to read")
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database=database_file, url_list_file=input_file)
