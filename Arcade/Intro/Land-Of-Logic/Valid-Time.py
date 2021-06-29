def validTime(time):
    rs = time.split(":")
    return 0<=int(rs[0])<=23 and 0<=int(rs[1])<=59 
