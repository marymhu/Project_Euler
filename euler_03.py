"""
Largest prime factor 
https://projecteuler.net/problem=3
"""
from math import sqrt


def largest_prime(value):
    # get prime number list from 2 to sqrt(value)
    prime_list = [2]
    max_val_prime = int(sqrt(value) + 1)
    # check only odd nb, 2 being prime
    for cur_nb in range(3, max_val_prime, 2):
        is_prime = True
        for cur_prime in prime_list:
            if cur_nb % cur_prime == 0:
                is_prime = False
        if is_prime:
            prime_list.append(cur_nb)
    # Get largest prime factor for value
    for prime in reversed(prime_list):
        if value%prime == 0:
            return prime
    return value


if __name__ == '__main__':
    print(largest_prime(600851475143))
