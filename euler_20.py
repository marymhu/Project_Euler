"""
Factorial digit sum
https://projecteuler.net/problem=20
"""
from time import time


def factorial_digit_sum (val):
    factorial = 1
    for i in range(2, val + 1):
        factorial *= i
    factorial_list = [int(x) for x in str(factorial)]
    return sum(factorial_list)


if __name__ == '__main__':
    assert 27 == factorial_digit_sum(10), "Error while checking test case 10!"
    # Compute result
    start = time()
    print(factorial_digit_sum(100))
    print("Execution time: " + str(time() - start))