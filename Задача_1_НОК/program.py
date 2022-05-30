# Найти НОК двух чисел


def Nok(numberFirst, numberSecond):
    primeFactorsFirst = []
    primeFactorsSecond = []
    nok = 1
    while(numberFirst != 1):
        for i in range(2, int(numberFirst+1)):
            if(numberFirst % i == 0):
                numberFirst = numberFirst/i
                primeFactorsFirst.append(i)
                break
    while(numberSecond != 1):
        for i in range(2, int(numberSecond+1)):
            if(numberSecond % i == 0):
                numberSecond = numberSecond/i
                primeFactorsSecond.append(i)
                break
    for i in primeFactorsFirst:
        nok *= i
        if(i in primeFactorsSecond):
            primeFactorsSecond.remove(i)
    for i in primeFactorsSecond:
        nok *= i
    return nok


d = Nok(68, 34)
print(d)
