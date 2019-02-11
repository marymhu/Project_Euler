"""
Lattice paths
https://projecteuler.net/problem=15
"""
from time import time


def lattice_path_length(size):
    # Intersections = nb sides + 1
    size += 1
    # Initialise count with the ones (vertical and horizontal sides of the grids)
    intersect_count_path = [0] * size * size
    for i in range(0, size):
        intersect_count_path[i] = 1
        intersect_count_path[i*size] = 1
    # Cumulates number of pathes until the last intersection
    # Only one half of the grid would be necessary but fast enough already
    for i in range(size + 1, size * size):
        if i % size != 0:
            intersect_count_path[i] = intersect_count_path[i-1] + intersect_count_path[i - size]
    return intersect_count_path[-1]


if __name__ == '__main__':
    start = time()
    print(lattice_path_length(20))
    print("Execution time: " + str(time() - start))
