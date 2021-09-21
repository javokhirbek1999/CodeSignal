import math
def countSumOfTwoRepresentations2(n, l, r):
    if 2*r < n or 2*l > n:
        return 0
    
    mi = max(l,n-r)
    ma = min(r,n-l)
    
    mid =  math.floor((ma+mi)//2)
    return mid-mi+1
