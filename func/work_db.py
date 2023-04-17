import sqlite3


def add_db(id):
    conn = sqlite3.connect('resourse/fg_db.db')
    cur = conn.cursor()
    cur.execute(f'INSERT INTO base(id, money) VALUES({id}, {1000})')
    conn.commit()


def choice_db(id, cashe):
    conn = sqlite3.connect("resourse/fg_db.db")
    cur = conn.cursor()
    cur.execute(f'UPDATE base '
                f'SET money = money + {cashe} '
                f'WHERE id = {id}')
    conn.commit()


def delete_db(id):
    conn = sqlite3.connect("resourse/fg_db.db")
    cur = conn.cursor()
    cur.execute(f'DELETE from base where id = {id}')
    conn.commit()


def get_db(id):
    conn = sqlite3.connect("resourse/fg_db.db")
    cur = conn.cursor()
    res = cur.execute(f'SELECT money FROM base where id = {id}')
    conn.commit()
    for title in res:
        return title[0]
