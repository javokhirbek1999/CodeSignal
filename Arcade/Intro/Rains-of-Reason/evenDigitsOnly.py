def evenDigitsOnly(n):
    if n<=0:
        return True
    if n%10!=0:
        if(n%10)%2!=0:
            return False
    if (n//10)%2!=0:
        return False
    return evenDigitsOnly(n//10)
        
