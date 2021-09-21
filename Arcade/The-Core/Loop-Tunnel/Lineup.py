def lineUp(commands):
    students = ['F','F','F','F']
    count = 0
    for i in commands:
        for j in range(len(students)):
            if i == 'L':
                if j == 1:
                    if students[j] == 'F':
                        students[j] = 'R'
                    elif students[j] == 'R':
                        students[j] = 'B'
                    elif students[j] == 'B':
                        students[j] = 'L'
                    elif students[j] == 'L':
                        students[j] = 'F'
                else:
                    if students[j] == 'F':
                        students[j] = 'L'
                    elif students[j] == 'L':
                        students[j] = 'B'
                    elif students[j] == 'B':
                        students[j] = 'R'
                    elif students[j] == 'R':
                        students[j] = 'F'
            elif i == 'R':
                if j == 1:
                    if students[j] == 'F':
                        students[j] = 'L'
                    elif students[j] == 'L':
                        students[j] = 'B'
                    elif students[j] == 'B':
                        students[j] = 'R'
                    elif students[j] == 'R':
                        students[j] = 'F'
                else:
                    if students[j] == 'F':
                        students[j] = 'R'
                    elif students[j] == 'R':
                        students[j] = 'B'
                    elif students[j] == 'B':
                        students[j] = 'L'
                    elif students[j] == 'L':
                        students[j] = 'F'
            else:
                pass
        if len(set(students)) == 1:
            count += 1
    return count
    
