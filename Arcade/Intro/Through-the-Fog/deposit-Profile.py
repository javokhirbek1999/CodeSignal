def depositProfit(deposit, rate, threshold):
    dep  = deposit
    years = 0
    r = 1+(rate/100)
    while dep <threshold:
        dep = dep*r
        years+=1
    return years
