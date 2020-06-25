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


