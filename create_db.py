'''
Script that initializes a sqLite database

SqLite doesn't contain a date data type, so dates are stored as integers. This should be something 
we keep in mind when we transition to a production environment and potentially a different DBMS

For the time being, dates should be stored as MMDDYYYY

Year should be stored as YYYY of the calandar year of the spring semester, i.e. the 2018-2019 school year should be stored as 2019

(These were decided to establish a consistent standard but if there's a reason to change them now is the time)
'''



import sqlite3

conn = sqlite3.connect('student.db')

c = conn.cursor()

c.execute('''
CREATE TABLE students (
    studentid integer,
    email text,
    first text,
    last text,
    dob text
)''')

conn.commit()

c.execute('''
CREATE TABLE classes (
    teacherid integer,
    year integer,
    studentid integer
)''')

conn.commit()

c.execute('''
CREATE TABLE scores (
    studentid integer,
    metricid integer,
    date integer,
    score integer
)''')

conn.commit()

conn.close()
