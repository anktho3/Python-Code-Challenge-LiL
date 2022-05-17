def primefactorize(numIn):
    primes = []
    numWork = int(numIn)
    factors = 2
    while numWork != 1:
        if (numWork % factors) == 0:
            primes.append(factors)
            numWork = numWork / factors
        else:
            factors += 1
    return primes

while True:
    numIn = input("Enter a positve integer: ")
    print(primefactorize(numIn))
