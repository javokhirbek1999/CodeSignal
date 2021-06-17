def circleOfNumbers(n, firstNumber):
    numbers = [i for i in range(n)]
    first_number_ind = numbers.index(firstNumber)
    re_arranged = numbers[first_number_ind:]
    rest = numbers[:first_number_ind]
    for i in rest:
        re_arranged.append(i)
    return re_arranged[(n//2)] 
