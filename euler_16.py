"""
Power digit sum
https://projecteuler.net/problem=16
"""
from time import time


def power_digit_sum(value):
    power_value_digits = [int(i) for i in str(2**value)]
    return sum(power_value_digits)


if __name__ == '__main__':
    # Check provided test case
    assert 26 == power_digit_sum(15), "Error while computing test case..."

    start = time()
    print(power_digit_sum(1000))
    print("Execution time: " + str(time() - start))
