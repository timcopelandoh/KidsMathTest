'''
Function to add records tp different tables in local test sqlite database
'''

import sqlite3


def add_student(studentid, email, first, last, dob, db='student.db', table='students'):
    '''
    Adds student record to existing database
    '''

    conn = sqlite3.connect(db)

    c = conn.cursor()

    sql = "INSERT INTO {} VALUES ({}, '{}', '{}', '{}', {})".format(table, studentid, email, first, last, dob)
    
    c.execute(sql)

    conn.commit()
    conn.close()
    




def add_class(teacherid, year, studentid, db='student.db', table='classes'):
    '''
    Adds student-teacher-year relationship to existing database
    '''

    conn = sqlite3.connect(db)

    c = conn.cursor()

    sql = "INSERT INTO {} VALUES ({}, {}, {})".format(table, teacherid, year, studentid)
    print(sql)
    c.execute(sql)

    conn.commit()
    conn.close()
    

def add_score(studentid, metricid, date, score, db='student.db', table='scores'):
    '''
    Adds score to existing database
    '''

    conn = sqlite3.connect(db)

    c = conn.cursor()

    sql = "INSERT INTO {} VALUES ({}, {}, {}, {})".format(table, studentid, metricid, date, score)

    print(sql)

    c.execute(sql)

    conn.commit()
    conn.close()
    

