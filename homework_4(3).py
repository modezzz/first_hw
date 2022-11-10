def sort_by_5(data: list) -> list:
    checkPoint = True
    for i in range(0, len(data), 5):
        data[i: i + 5] = sorted(data[i: i + 5]) if checkPoint else sorted(data[i: i + 5], reverse=True)
        checkPoint = not checkPoint
    return data

lst = [32, 43, 1, 3, 4, 5, 34, 5, 1, 7, 10, 34, 17, 11, 10, -2, 4, 5, 10, 11]
#lst = [5,4,3,2,1,1,2,3,4,5]

print(sort_by_5(lst))

