import sqlite3

conn = sqlite3.connect('pybook.db')

cursor = conn.cursor()

SQL = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, '\
    'username TEXT NOU NULL, email TEXT NOT NULL, passwd TEXT NOT NULL, authkey TEXT)'
    
cursor.execute(SQL)


cursor.close()
conn.close()    