import sqlite3



def db_connect():
    conn = sqlite3.connect('myPollyDB.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS `birds` (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, species TEXT, lname TINYTEXT, number CHAR(6), year CHAR(4), month CHAR(2), day CHAR(2), hour CHAR(2), city TINYTEXT, country TINYTEXT, habitat TINYTEXT, xcoordinates CHAR(10), ycoordinates CHAR(10), notes TINYTEXT, author TINYTEXT)")
    conn.commit()
    conn.close()

def insert(species,lname,number,year,month,day,hour,city,country,habitat,xcoordinates,ycoordinates,notes,author):
    conn = sqlite3.connect('myPollyDB.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO birds VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(species,lname,number,year,month,day,hour,city,country,habitat,xcoordinates,ycoordinates,notes,author))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('myPollyDB.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM birds")
    rows = cur.fetchall()
    conn.close()

db_connect()