import datetime

def modify_date(date):
    
    '''
    Transforms date in integer format to python datetime
    '''

    return datetime.date(date % 10000, date // 1000000, (date % 1000000) // 10000)
