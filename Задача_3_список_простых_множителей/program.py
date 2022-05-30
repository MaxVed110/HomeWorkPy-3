# Составить список простых множителей натурального числа N

def PrimeFactorsNumbers(number):
    primeFactors = []
    while(number != 1):
        for i in range(2, int(number+1)):
            if(number % i == 0):
                number = number/i
                primeFactors.append(i)
                break
    return primeFactors


primeFactorsUser = PrimeFactorsNumbers(68)
print(primeFactorsUser)
