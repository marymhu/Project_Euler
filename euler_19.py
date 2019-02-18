"""
Counting Sundays
https://projecteuler.net/problem=19
"""
from time import time


def counting_sundays ():
    list_31 = [1, 3, 5, 7, 8, 10, 12]
    list_30 = [4, 6, 9, 11]
    day_count = 0
    sunday_count = 0
    for year in range(1900, 2001):
        for month in range(1,13):
            if month in list_31:
                month_length = 31
            elif month in list_30:
                month_length = 30
            else:
                # February days: Leap Year ?
                month_length = 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28
            for day in range(1, month_length + 1):
                day_count += 1
                if day_count % 7 == 0 and day == 1 and year > 1900:
                    sunday_count += 1
    return sunday_count


if __name__ == '__main__':
    # Compute result
    start = time()
    print(counting_sundays())
    print("Execution time: " + str(time() - start))