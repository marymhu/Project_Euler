"""
Summation of primes
https://projecteuler.net/problem=10
"""


def compute_prime_sum(max_val):
    """
    Compute the sum of the prime numbers below max_val using the Sieve of Eratosthenes
    """
    candidates = [x for x in range(2, max_val) if x <= 3 or x % 2 != 0 or x % 3 != 0]
    sum_prime = 0
    while candidates:
        current = candidates[0]
        sum_prime += current
        candidates = [x for x in candidates if x > current and x % current != 0]
    return sum_prime


if __name__ == '__main__':
    # Provided test case
    assert 17 == compute_prime_sum(10)

    # Get Result
    print(compute_prime_sum(2000000))
