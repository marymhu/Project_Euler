"""
Summation of primes
https://projecteuler.net/problem=10
"""


def compute_prime_sum(max_val):
    """
    Compute the sum of the prime numbers below max_val
    """
    prime_list = [2, 3]
    cur_val = prime_list[-1]
    while cur_val < max_val:
        cur_val += 2
        is_prime = True
        for p in prime_list:
            if cur_val % p == 0:
                is_prime = False
                break
        if is_prime and cur_val < max_val:
            prime_list.append(cur_val)
    return sum(prime_list)


if __name__ == '__main__':
    # Provided test case
    assert 17 == compute_prime_sum(10)
    
    # Get Result
    print(compute_prime_sum(2000000))