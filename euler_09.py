"""
Special Pythagorean triplet
https://projecteuler.net/problem=9
"""


def is_pythagorean_triplet(x, y, z):
    if (x * x) + (y * y) == z * z and x < y and y < z:
        return True
    else:
        return False


def triplet(triplet_sum):
    """
    Find Pythagorean Triplet with a+b+c = triplet_sum
    Return a*b*c
    """
    for a in range(1, triplet_sum - 3):
        for b in range(a, triplet_sum - 3):
            for c in range(b, triplet_sum - 3):
                if is_pythagorean_triplet(a, b, c):
                    if a + b + c == triplet_sum:
                        return a * b * c
    return 0


if __name__ == '__main__':
    print(triplet(1000))