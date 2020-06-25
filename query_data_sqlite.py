import sqlite3
import pandas as pd

def report_student(studentid, db='student.db', table='scores'):
    '''
    Return all score records associated with a certain studentid
    '''
    conn = sqlite3.connect(db)

    c = conn.cursor()

    sql = """
    SELECT *
    FROM {}
    WHERE studentid = {}
    """.format(table, studentid)
    
    c.execute(sql)

    df = pd.DataFrame(c.fetchall())

    conn.commit()
    conn.close()

    return df


def report_class(teacherid, year=2020, db='student.db', class_table='classes', score_table='scores'):
    '''
    Return all score records associated with a certain classroom
    '''
    conn = sqlite3.connect(db)

    c = conn.cursor()

    sql = """
    SELECT *
    FROM {}
    WHERE studentid IN (
        SELECT studentid
        FROM {}
        WHERE teacherid = {}
        )
    """.format(score_table, class_table, teacherid)
    
    c.execute(sql)

    df = pd.DataFrame(c.fetchall())

    conn.commit()
    conn.close()

    return df



