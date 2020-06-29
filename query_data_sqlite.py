import sqlite3
import pandas as pd
import transform_data

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
    
    df.rename(columns={0: 'studentid', 1:'metricid', 2:'date', 3:'score'}, inplace=True)

    df['date'] = df['date'].apply(transform_data.modify_date)

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

def class_list(teacherid, year=2020, db='student.db', class_table='classes', student_table='students'):
    '''
    Return all score records associated with a certain classroom
    '''
    conn = sqlite3.connect(db)

    c = conn.cursor()

    sql = """
        SELECT c.studentid, s.first, s.last
        FROM {} AS c
        LEFT OUTER JOIN
        {} as s
        ON c.studentid = s.studentid
        WHERE c.teacherid = {}
    """.format(class_table, student_table, teacherid)
   



    c.execute(sql)

    df = c.fetchall()

    conn.commit()
    conn.close()

    return df

