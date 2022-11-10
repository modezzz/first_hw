def sort_by_param(data: list, start: int, finish: int) -> list:
    for i in range(0, len(data)):
        data[start: finish] = sorted(data[start: finish])
    return data


lst = [32, 43, 1, 3, 4, 5, 34, 5, 1, 7, 10, 34, 17, 11, 10, -2, 4, 5, 10, 11]
#lst = [5,4,3,2,1,1,2,3,4,5]


print(sort_by_param(lst, 7, -2))

print(lst[7:-2])