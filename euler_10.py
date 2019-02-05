"""
Summation of primes
https://projecteuler.net/problem=10
"""


def compute_prime_sum(max_val):
    """
    Compute the sum of the prime numbers below max_val using the Sieve of Eratosthenes
    """
    candidates = [True] * max_val
    sum_prime = 0
    for val in range(2, max_val):
        if candidates[val]:
            sum_prime += val
            for m in range(val * val, max_val, val):
                candidates[m] = False            
    return sum_prime


if __name__ == '__main__':
    # Provided test case
    assert 17 == compute_prime_sum(10)

    # Get Result
    print(compute_prime_sum(2000000))
