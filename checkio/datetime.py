def days_diff(a, b):
    import datetime 
   
    date_one=datetime.datetime(a[0], a[1], a[2])
    date_two= datetime.datetime(b[0], b[1], b[2])
    a= date_two - date_one
    
    return abs(a.days)