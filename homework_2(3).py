def multiples_check():
    """Replacing digits by a [str] data type"""
    fizz = int(input('Enter first number: '))
    buzz = int(input('Enter second number: '))
    hardbazz = int(input('Enter third number: '))
    for num in range(1, hardbazz + 1):
        if num % buzz == 0 and num % fizz == 0:
            num = 'FB'
        elif num % buzz == 0:
            num = 'B'
        elif num % fizz == 0:
            num = 'F'
        print(num, end='')


multiples_check()


