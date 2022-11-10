def workWithFile():
    fizz = int(input('Enter first number: '))
    buzz = int(input('Enter second number: '))
    fileRead = open("file_1.txt", mode='rt')
    lines = fileRead.readlines()
    for line in lines:
        for num in line.split():
            if int(num) % buzz == 0 and int(num) % fizz == 0:
                num = 'FB'
            elif int(num) % buzz == 0:
                num = 'B'
            elif int(num) % fizz == 0:
                num = 'F'
            print(num, end=' ')


workWithFile()






