import sqlite3

def connect_db(conn):
    return conn.cursor()

def drop_table(cursor):
    sql = """DROP TABLE IF EXISTS editor"""
    cursor.execute(sql)

def create_table(cursor):
    drop_table(cursor)
    sql = """CREATE TABLE IF NOT EXISTS editor
            (name TEXT,
            developer TEXT,
            release INTEGER)
            """
    cursor.execute(sql)

def insert_data(cursor, data):
    sql = f"""INSERT INTO editor
        VALUES {data}"""
    cursor.execute(sql)

def select_data(cursor):
    sql = """SELECT * FROM editor"""
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

if __name__ == '__main__':
    conn = sqlite3.connect('editors.db')
    cursor = connect_db(conn)
    create_table(cursor)
    data = [('Acme','Rob Pike',1993),
    ('AkelPad','Alexey KuznetsovAlexander Shengalts',2003),
    ('Alphatk','Vince Darley',1999)]
    for row in data:
        insert_data(cursor, row)
        conn.commit()
    select_data(cursor)
