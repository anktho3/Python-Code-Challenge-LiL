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

    
numIn = input("Enter a positve integer: ")
while len(numIn) > 0:
    print(primefactorize(numIn))
    numIn = input("\nEnter a positve integer: ")

