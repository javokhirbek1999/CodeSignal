def phoneCall(min1, min2_10, min11, s):
    if s<min1:
        return 0
    max_mins = s
    max_possible_mins = 0
    if max_mins-min1>0:
        max_possible_mins+=1
        max_mins = max_mins-min1
    min3_to_10 = min2_10
    while True:
        for i in range(9):
            if max_mins<min3_to_10:
                return max_possible_mins
            max_mins = max_mins-min3_to_10
            max_possible_mins+=1
            if max_mins<min3_to_10 or max_mins==0:
                return max_possible_mins
        while True:
            if max_mins<min11:
                return max_possible_mins
            max_mins = max_mins-min11
            max_possible_mins+=1
        return max_possible_mins
    return max_possible_mins
        

