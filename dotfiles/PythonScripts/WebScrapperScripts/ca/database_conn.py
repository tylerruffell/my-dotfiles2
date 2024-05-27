import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def drop_table(conn):
    """ drop a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    sql = """ DROP TABLE IF EXISTS info;""" 
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)


def create_table(conn):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    sql = """ CREATE TABLE IF NOT EXISTS info (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    birth TEXT NOT NULL,
                                    death TEXT,
                                    term_from TEXT NOT NULL,
                                    term_to TEXT 
                                ); """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

def insert_data(conn, data):
    """Insert data records into the info table

    Args:
        conn (connection object): Connection object
        data (tuple): Data record
    """
    # TODO: Complete this task
    pass


def select_data(conn):
    """Select inserted data from info table

    Args:
        conn (connection object): Connection object
    """
    cur = conn.cursor()
    cur.execute('SELECT * FROM info')
    rows = cur.fetchall()
    if len(rows) == 0:
        print('No records available')
    # loop over records
    for row in rows:
        print(row)

