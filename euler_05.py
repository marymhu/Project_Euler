"""
Smallest Multiple
https://projecteuler.net/problem=5
"""


def smallest_multiple(max_term):
    """
    Find smallest multiple of numbers between 1 .. max_term
    """
    value = max_term
    found = False
    while not found:
        for div in range(max_term, 1, -1):
            found = True
            if value % div != 0:
                found = False
                break
        if not found:
            value += max_term
    return value


if __name__ == '__main__':
    assert 2520 == smallest_multiple(10),\
        "Error while computing smallest multiple of numbers 1 .. 10"
    print(smallest_multiple(20))
