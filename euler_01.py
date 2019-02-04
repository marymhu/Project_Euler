"""
Multiples of 3 and 5
https://projecteuler.net/problem=1
"""


def multiples():
    mult_list = []
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            mult_list.append(i)
    return sum(mult_list)


if __name__ == '__main__':
    print(multiples())
