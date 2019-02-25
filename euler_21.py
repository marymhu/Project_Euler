"""
Amicable Numbers
https://projecteuler.net/problem=21
"""

from time import time


def divisors_sum(number):
    """
    Find the sum of "number" divisors
    """
    sum_div = 1
    # Divisors going by pair (p*q or q*p), we only look for divisors from 1 to value
    for div in range (2, int(number ** 0.5) + 1):
        if number % div == 0:
            sum_div += div
            if div * div != number:
                sum_div += number/div
    return sum_div

 
if __name__ == '__main__':
    # Check the divisors_sum function
    assert 284 == divisors_sum(220)
    assert 220 == divisors_sum(284)
    
    start = time()
    sum_table = [0] * 10001
    sum_table[1] = 1
    for i in range(2, 10000):
        sum_table[i] = divisors_sum(i)
    
    sum_amicable = 0
    for i,j in enumerate(sum_table):
        if j < 10000:
            if sum_table[i] == j and sum_table[j] == i and i != j:
                sum_amicable += i + j
    # Amicable numbers go by pair => divide by two
    print("Sum of amicable numbers until 10000: " + str(sum_amicable/2))
    print("Execution time: " + str(time() - start))
