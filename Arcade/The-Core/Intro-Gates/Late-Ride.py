from datetime import datetime, timedelta
def lateRide(n):
    datetime_original = datetime(2021,7, 7, 00,00,00)
    new = datetime_original+timedelta(minutes=float(n))
    new_time = str(new.time())
    s = 0
    for i in new_time.split(":"):
        for j in i:
            if j.isdigit():
                s+=int(j)
    return s
            
