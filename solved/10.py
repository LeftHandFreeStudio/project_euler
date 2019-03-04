# -*- coding: utf-8 -*-

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

import math

def is_prime_number(x):
    if x < 2:
        return False
    elif x == 2 or x == 3:
        return True
    elif x == 4:
        return False
    else:
        if x % 2 == 0:
            return False
        for y in range(3,math.ceil(math.sqrt(x)+1),2):
            if (x % y == 0):
                return False
        return True
    
def solutions():
    sumOfPrimes = 0
    for i in range(2,2000000):
        if  is_prime_number(i):
            sumOfPrimes += i
    print(sumOfPrimes)




if __name__ == "__main__":	
	solutions() 