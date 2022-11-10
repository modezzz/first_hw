def creating_lists(data_storage: list):
    operation = int(input('''
    Available operations:
    1)Output the elements with paired indexes.
    2)Output the sum of all elements.
    3)Output the sum of all paired elements.
    4)Output the sum of all unpaired elements.
    5)Output the largest element with index.
    Choose the desired operation(digit): '''))
    if operation == 1:
        dataPaired = [num for index, num in enumerate(data_storage) if index % 2 == 0]
        print(f'All paired indexes from list with elements: "{dataPaired}".')
    elif operation == 2:
        dataSum = sum(data_storage)
        print(f'The sum of all elements: "{dataSum}".')
    elif operation == 3:
        pairedSum = sum([num for num in data_storage if num % 2 == 0])
        print(f'The sum of all paired elements: "{pairedSum}".')
    elif operation == 4:
        unpairedSum = sum([num for num in data_storage if num % 2 != 0])
        print(f'The sum of all unpaired elements: "{unpairedSum}".')
    elif operation == 5:
        maxNum = max(data_storage)
        maxIndex = data_storage.index(maxNum)
        print(f'The largest number is "{maxNum}", with index "{maxIndex}".')
    else:
        print('Incorrect choice!\nPlease try again.')


creating_lists([1, 3, 5, 2, 4, 6, 7, 9, 11, 42, -2.5])