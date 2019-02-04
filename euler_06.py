"""
Sum square difference
https://projecteuler.net/problem=6
"""


def sum_square(max_term):
    """
    Sum of the squares of the first max_term natural numbers
    """
    sum_sq = 0
    for i in range(1, max_term+1):
        sum_sq += i * i
    return sum_sq


def square_sum(max_term):
    """
    Square of the sum of the first max_term natural numbers
    """
    sq_sum = 0
    for i in range(1, max_term+1):
        sq_sum += i
    return sq_sum * sq_sum


if __name__ == '__main__':
    # Check provided test case
    assert 2640 == (square_sum(10) - sum_square(10)),\
        "Error while computing Sum square difference for 10 first natural numbers"
    # Get result
    print(str(square_sum(100) - sum_square(100)))
