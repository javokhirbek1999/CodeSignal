def magicalWell(a, b, n):
    
    total = 0
    
    a1 = a
    b1 = b
    
    for i in range(n):
        total += (a1*b1)
        a1+=1
        b1+=1
            
    return total
