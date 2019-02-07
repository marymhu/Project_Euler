"""
Highly divisible triangular number
https://projecteuler.net/problem=12
"""


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
    divisors = []
    while len(divisors) < divisor_number - 1:
        current_rank, current_triangle_value = generate_next_triangle(current_rank, current_triangle_value)
        divisors = [num for num in range(1, current_triangle_value) if current_triangle_value % num == 0]
    return current_triangle_value


if __name__ == '__main__':
    # Check provided test case
    assert 28 == find_divisible_triangle(5),\
        "Error while computing the first triangle number to have over 5 divisors"
    # Get Result
    find_divisible_triangle(500)