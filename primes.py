"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(number):

    for x in range(2, number):
        
        if number%x == 0:
            return False
    return True
                   

def primes(number_of_primes):

    if number_of_primes < 1:
        raise ValueError
    
    listOfPrimes = []
    number = 2
    
    while len(listOfPrimes) < number_of_primes:
        
        if isPrime(number):
            listOfPrimes.append(number)
        number+=1

    return listOfPrimes
 
    
