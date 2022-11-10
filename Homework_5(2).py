with open('file_2.txt') as fl:
    line = fl.read().split('\n')
    newData = []
    for elem in line:
        try:
            resLine = eval(elem)
            newData.append(resLine)
        except ZeroDivisionError:
            newData.append('Division by zero')
    print(newData)


with open('file_2.txt', 'w') as fls:
    for line in fls.readline():
        fls.write('\n'.join(newData))




