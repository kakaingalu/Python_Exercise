#!/usr/bin/python3
# A prime can only be divided by 1 and itself
# 5 is a prime 1 and 5 = positive factor 
# 6 is not prime 1, 2, 3, 6

# Input max prime
# Use a for loop and check if modules == True

def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False

    return True

def getPrimes(max_number):
    list_of_primes = []

    for num1 in range(2, max_number):
        if is_prime(num1):
            list_of_primes.append(num1)

    return list_of_primes

max_num_to_check = int(input("Search for primes up to: "))

list_of_primes = getPrimes(max_num_to_check)

for prime in list_of_primes:
    print(prime)
