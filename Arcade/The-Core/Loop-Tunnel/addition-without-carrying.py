def additionWithoutCarrying(param1, param2):
    max_len = len(str(param1)) if len(str(param1))>len(str(param2)) else len(str(param2))
    
    par1 = [0]*max_len 
    par2 = [0]*max_len
    
    t = -1
    for i in reversed(list(str(param1))):
        par1[t] = int(i)
        t -= 1
    
    t = -1
    
    for i in reversed(list(str(param2))):
        par2[t] = int(i)
        t -= 1
    total = []
    for i in range(len(par1)):
        temp = par1[i]+par2[i]
        total.append(str(temp%10))
    
    return int("".join(total))
