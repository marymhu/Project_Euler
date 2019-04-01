"""
Names scores
https://projecteuler.net/problem=22
"""

from time import time


def names_scores(filepath):
    """
    Sort, format and compute the score of each name.
    Sum the results and returns the total value.
    """
    file = open(filepath)
    names = file.readline()
    file.close()
    names = names.replace("\"", "")
    name_list = names.split(",")
    name_list.sort()
    sum_score = 0
    for idx, name in enumerate(name_list):
        score = sum([(ord(char) - ord('A') + 1) for char in name])
        score = score * (idx + 1)
        sum_score += score
    return sum_score

 
if __name__ == '__main__':
    start = time()
    print(names_scores("p022_names.txt"))
    print("Execution time: " + str(time() - start))