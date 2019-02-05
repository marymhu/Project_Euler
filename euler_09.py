"""
Special Pythagorean triplet
https://projecteuler.net/problem=9
"""


def is_pythagorean_triplet(x, y, z):
    if (x * x) + (y * y) == z * z and x < y and y < z:
        return True
    else:
        return False


def triplet():
    """
    Find Pythagorean Triplet with a+b+c = 1000
    Return a*b*c
    """
    for a in range(1, 1000):
        for b in range(1, 1000):
            for c in range(1, 1000):
                if is_pythagorean_triplet(a, b, c):
                    if a + b + c == 1000:
                        return a * b * c
    return 0

if __name__ == '__main__':
    print(triplet())