def creatingBox():
    infoFromUser = int(input('Enter the dimensions of the box: '))
    print('#' * infoFromUser)
    for elem in range(infoFromUser - 2):
        print('#' + ' ' * (infoFromUser - 2) + '#')
    print('#' * infoFromUser)


creatingBox()


