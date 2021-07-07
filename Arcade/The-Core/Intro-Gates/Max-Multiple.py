def maxMultiple(divisor, bound):
    t = []
    for i in range(9999999999):
        if i%divisor==0 and 0<i<=bound:
            t.append(i)
        if i>bound:
            return max(t)
