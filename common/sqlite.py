#!/bin/python


import sqlite3

def sqliteconnect(dbfile):
    conn = sqlite3.connect(dbfile)
    print "Opened database successfully";


def sqlitecreatetable(conn):
    conn.execute('''CREATE TABLE COMPANY
             (ID INT PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL,
             AGE            INT     NOT NULL,
             ADDRESS        CHAR(50),
             SALARY         REAL);''')
    print "Table created successfully";
    conn.close()

def sqliteselect():
    print "select"