"""
Highly divisible triangular number
https://projecteuler.net/problem=12
"""
from time import time

def generate_next_triangle(rank, val):
    """
    Generate the next triangle number
    """
    return rank + 1, val + rank + 1


def find_divisible_triangle(divisor_number):
    """
    Find the first triangle number to have over divisor_number divisors
    """
    current_rank = 1
    current_triangle_value = 1
    divisors = 0
    while divisors < divisor_number - 1:
        current_rank, current_triangle_value = generate_next_triangle(current_rank, current_triangle_value)
        divisors = 0
        # Divisors going by pair (p*q or q*p), we only look for divisors from 1 to value
        for div in range (2, int(current_triangle_value ** 0.5) + 1):
            if current_triangle_value % div == 0:
                # if div is sqrt(value), only one divisors is found
                if (div * div == current_triangle_value):
                    divisors += 1
                else:
                    divisors += 2
    return current_triangle_value


if __name__ == '__main__':
    # Check provided test case
    assert 28 == find_divisible_triangle(5),\
        "Error while computing the first triangle number to have over 5 divisors"
    # Get Result
    start = time()
    print(find_divisible_triangle(500))
    print("Exectution time: " + str(time() - start))
