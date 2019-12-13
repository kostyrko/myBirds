import sqlite3


def db_connect():
    conn = sqlite3.connect('myPollyDB.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS `birds` (id INTEGER PRIMARY KEY, species text, lname text, year integer, month integer, day integer, hour integer,number integer, city text, country text, habitat text, xcoordinates integer, ycoordinates integer, notes text, author text)")
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

def search(species='',lname='',year='',month='',day='',hour='',number='',city='',country='',habitat='',xcoordinates='',ycoordinates='',notes='',author=''):
    conn = sqlite3.connect('myPollyDB.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM birds WHERE species=? OR lname=? OR year=? OR month=? OR day=? OR hour=? OR number=? OR city=? OR country=? OR habitat=? OR xcoordinates=? OR ycoordinates=? OR notes=? OR author=?",(species,lname,year,month,day,hour,number,city,country,habitat,xcoordinates,ycoordinates,notes,author))
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