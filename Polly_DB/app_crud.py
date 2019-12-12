import sqlite3


def db_connect():
    conn = sqlite3.connect('myPollyDB.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS `birds` (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, species TEXT, lname TINYTEXT, year CHAR(4), month CHAR(2), day CHAR(2), hour CHAR(2),number CHAR(6), city TINYTEXT, country TINYTEXT, habitat TINYTEXT, xcoordinates CHAR(10), ycoordinates CHAR(10), notes TINYTEXT, author TINYTEXT)")
    conn.commit()
    conn.close()


def insert(species,lname,year,month,day,hour,number,city,country,habitat,xcoordinates,ycoordinates,notes,author):
    conn = sqlite3.connect('myPollyDB.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO birds VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(species,lname,year,month,day,hour,number,city,country,habitat,xcoordinates,ycoordinates,notes,author))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('myPollyDB.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM birds")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(species="",lname="",year="",month="",day="",hour="",number="",city="",country="",habitat="",xcoordinates="",ycoordinates="",notes="",author=""):
    conn = sqlite3.connect('myPollyDB.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM birds WHERE species=? OR lname=? OR year=? OR month=? OR day=? OR hour=? OR number=? OR city=? OR country=? OR habitat=? OR xcoordinates=? OR ycoordinates=? OR notes=? OR author=?")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('myPollyDB.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM birds WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id,species,lname,year,month,day,hour,number,city,country,habitat,xcoordinates,ycoordinates,notes,author):
    conn = sqlite3.connect('myPollyDB.db')
    cur = conn.cursor()
    cur.execute("UPDATE birds SET species=?,lname=?,year=?,month=?,day=?,hour=?,number=?,city=?,country=?,habitat=?,xcoordinates=?,ycoordinates=?,notes=?,author=? WHERE id=?",(species,lname,year,month,day,hour,number,city,country,habitat,xcoordinates,ycoordinates,notes,author,id))
    conn.commit() 
    conn.close()

db_connect()