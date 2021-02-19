import sqlite3
global curs
global conn
conn=sqlite3.connect("database.db")
curs=conn.cursor()

#Create spor table
curs.execute("CREATE TABLE IF NOT EXISTS athletes(\
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
tcId TEXT NOT NULL UNIQUE,\
firstName TEXT NOT NULL,\
lastName TEXT NOT NULL,\
sportClub TEXT NOT NULL,\
athleteWeight TEXT NOT NULL,\
athleteGender TEXT NOT NULL,\
maritalStatus TEXT NOT NULL,\
branchOfSport TEXT NOT NULL,\
birthday TEXT NOT NULL)")

conn.commit()

