"""
Longest Collatz sequence
https://projecteuler.net/problem=14
"""
from time import time


def compute_collatz_sequence(start, possible_result):
    current_value = start
    seq_size = 1
    while current_value != 1:
        if current_value < start:
            possible_result[current_value] = False
        current_value = int(current_value / 2) if current_value % 2 == 0 else current_value * 3 + 1
        seq_size += 1
    return seq_size


def longest_sequence(max_val):
    possible_result = [True] * max_val
    max_seq_size = 0
    result = 0
    for i in range(2, max_val):
        if possible_result[i]:
            current_size = compute_collatz_sequence(i, possible_result)
            max_seq_size, result = (current_size, i) if current_size > max_seq_size else (max_seq_size, result)
    return result


if __name__ == '__main__':
    start = time()
    print(longest_sequence(1000000))
    print("Execution time: " + str(time() - start))
