import sqlite3

conn = sqlite3.Connection('AZIZA_BAKERY.db')
cur = conn.cursor()

def create_table(dp):
    query = """CREATE TABLE IF NOT EXISTS MENYU(
user_id INTEGER,
telefon VARCHAR(50),
razmer VARCHAR(50),
tort VARCHAR(50)
);"""
    cur.execute(query)
    conn.commit()


def insert_data(data):
    query = """INSERT INTO MENYU(user_id,telefon,razmer,tort)
            VALUES
            (?, ?, ?, ?);
            """
    cur.execute(query, data)
    conn.commit()


def select():
    query = """SELECT * MENYU;"""
    cur.execute(query)
    return cur.fetchall()



def select_data(user_id):
    query = f"""SELECT * FROM MENYU WHERE user_id={user_id};"""
    cur.execute(query)
    return cur.fetchall()