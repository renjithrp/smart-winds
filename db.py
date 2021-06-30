
import sqlite3
from sqlite3 import Error
from config import DATABASE_NAME


CREATE_TABLE_QUERY = """ CREATE TABLE IF NOT EXISTS data (
                                        id integer primary key autoincrement ,
                                        spool_width NUMERIC, 
                                        spool_diaz NUMERIC, 
                                        wire_guage NUMERIC, 
                                        no_of_turns NUMERIC,
                                        int_position NUMERIC, 
                                        turns_count NUMERIC, 
                                        pos_reach NUMERIC, 
                                        mode INTEGER
                                    ); """

def create_connection():
    db_file = DATABASE_NAME + ".db"
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def get_connection():
    conn = create_connection()
    if conn is not None:
        create_table(conn, CREATE_TABLE_QUERY)
        return conn
    else:
        print("Database connection error!!")

conn = get_connection()

def update(values):

    columns = ', '.join(values.keys())
    placeholders = ', '.join('?' * len(values))
    sql = 'INSERT INTO data ({}) VALUES ({})'.format(columns, placeholders)
    values = [int(x) if isinstance(x, bool) else x for x in values.values()]
    c = conn.cursor()
    c.execute(sql, values)
    return True
    

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def fetch():
    sql = "select * from data ORDER BY id DESC;"
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(sql)
    return c.fetchone()

