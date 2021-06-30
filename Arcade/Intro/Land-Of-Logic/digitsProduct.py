import time
def digitsProduct(product):
    i = 1
    start = time.time()
    while True:
        temp = list(str(i))
        temp = [int(j) for j in temp]
        pr = 1
        for j in range(len(temp)):
            pr*=temp[j]
        if pr == product:
            return i
        i+=1
        end = time.time()
        if end-start > 0.1:
            return -1
