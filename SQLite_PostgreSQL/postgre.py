import psycopg2 as db


def create_table():
    conn = db.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = db.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = db.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    conn.close()
    return rows



create_table()