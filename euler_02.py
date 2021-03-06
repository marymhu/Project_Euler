"""
Sum of even-valued Fibonacci terms under 4_000_000 
https://projecteuler.net/problem=2
"""


def fibonacci(max_val):
    """
    Sum of even-valued Fibonacci terms under max_val
    """
    # Init with first terms
    a, b = 1, 2
    sum_fib = 2
    next_term = a + b
    while next_term < max_val:
        sum_fib = sum_fib + next_term if next_term % 2 == 0 else sum_fib
        a, b = b, next_term
        next_term = a + b
    return sum_fib


if __name__ == '__main__':
    print(fibonacci(4000000))
