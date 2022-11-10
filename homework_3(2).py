def someMethods():
    data = input('Enter smth what you want: ')
    if 5 <= len(data) <= 15:
        dataSlice = data[len(data) // 2:] + data[:len(data) // 2]
        dataSliceElements = dataSlice[len(dataSlice) - 3:len(dataSlice) + 1]
        print(dataSlice.replace(dataSliceElements, dataSliceElements.upper()))
    else:
        print('You can enter enter at least 5 but not more than 15 characters!\nPlease try again.')


someMethods()