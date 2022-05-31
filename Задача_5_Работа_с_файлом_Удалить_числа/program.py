# Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.

def DeleteFromFile(name):
    data = open(name, 'r')
    newStringNumbers = ''
    for line in data:
        stringNumbers = ''
        stringNumbers += line
        listNumbers = stringNumbers.split(' ')
        for i in range(listNumbers.__len__()):
            if listNumbers[i].isnumeric():
                if int(listNumbers[i]) % 2 != 0:
                    newStringNumbers += f"{listNumbers[i]} "
        newStringNumbers += "\n"
    data = open(name, 'w')
    data.writelines(newStringNumbers)
    data.close


name = 'file.txt'
DeleteFromFile(name)
