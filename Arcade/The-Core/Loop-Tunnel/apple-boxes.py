def appleBoxes(k):
    red, yellow = 0,0
    
    for i in range(1,k+1):
        if i%2==0:
            red+=i*i
        else:
            yellow+=i*i
    
    return red-yellow
