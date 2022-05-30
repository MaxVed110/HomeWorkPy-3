# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

import itertools


def SortFirst(listUser):
    newListFirst = []
    for i in listUser:
        if i not in newListFirst:
            newListFirst.append(i)
    return newListFirst


def SortSecond(listUser: list):
    listUser.sort()
    newListSecond = [i for i, _ in itertools.groupby(listUser)]
    return newListSecond


listUser = [1, 4, 1, 5, 1, 5, 3, 10]
newListFirst = SortFirst(listUser)
newListSecond = SortSecond(listUser)
print(newListFirst)
print()
print(newListSecond)
