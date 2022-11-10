def findingTheMiddle():
    basketWithData = []
    first_str = input('Enter smth: ')
    basketWithData.append(first_str)
    second_str = input('Enter smth again: ')
    basketWithData.append(second_str)
    third_str = input('And again: ')
    basketWithData.append(third_str)
    for elements in basketWithData:
        temp = len(elements) // 2
        if len(elements) % 2:
            print(f"The middle of string '{elements}' it`s symbol: '{elements[temp]}'")
        else:
            print(f"The middle of string '{elements}' it`s symbols: '{elements[temp - 1]}' and '{elements[temp]}'")


findingTheMiddle()

        











