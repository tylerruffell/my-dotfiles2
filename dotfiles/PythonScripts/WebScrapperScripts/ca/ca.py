from argparse import ArgumentParser
import requests
from bs4 import BeautifulSoup
import pandas as pd 
import sqlite3
import database_conn as db # your local database connection
import io  # To suppress the pandas read_html() warning

def extract_wiki_info(wiki_page):
    """Extract table data from a wiki_page

    Args:
        wiki page (string): url address of wiki page

    Returns:
        dataFrame: a Pandas data frame with wiki table info
    """
    page = requests.get(wiki_page)
    print(f'Page Acces status {page.status_code}')

    bs = BeautifulSoup(page.text, 'html.parser')
    table = bs.find('table', {'class':'wikitable'})
    df = pd.read_html(io.StringIO(str(table)))[0]
    print(df)
    return df

def data_wrangling(df):
    """Convert pandas data frame to a list of dictionaries with filter data

    Args:
        df (pandas dataFrame): dataFrame with wiki page table information

    Returns:
        list: list of dictionaries with filter data
    """
    # TODO: Complete this task
    pass

def main():
    # Task 1: Take input parameter with getopt

    parser = ArgumentParser(prog='optinoal arguments')
    parser.add_argument('-d', '--database', action='store', help="Specify the database")
    options = parser.parse_args()
    
    # create a database connection

    conn = db.create_connection(options.database)

    #create tables
    if conn is not None:
        print("SUCCESS! database connection.")
        # create projects table
        db.drop_table(conn)
        db.create_table(conn)
    else:
        print("Error! cannot create the database connection.")
        
    # Task 2: Wiki Page Data Extraction    
    # Wiki page to analyze. DO NOT REMOVE 
    wiki_page = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
            
    president_df = extract_wiki_info(wiki_page)
    
    # Task 3: Data wrangling
    # president_info = data_wrangling(president_df)

    # Task 4: Store data in your sqlite table
    
    # Uncomment the following line when you are ready
    # to test your code
    # db.select_data(conn) 


if __name__ == '__main__':
    main()
