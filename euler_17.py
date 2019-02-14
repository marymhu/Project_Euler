"""
Number Letter Count
https://projecteuler.net/problem=17
"""
from time import time


def number_letter_count (max_num):
    under_20 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    multiple_ten = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    letter_sum = 0
    for i in range (1, max_num + 1):
        units = i%10
        tens = (i//10) % 10
        hundreds = (i//100) % 10

        str_num = ""
        if i == 1000:
            str_num += "one" + "thousand"
        else:
            if hundreds != 0:
                str_num += under_20[hundreds - 1] + "hundred"
                if i%100 != 0:
                    str_num += "and"
            if i%100 != 0:
                if tens < 2:
                    str_num += under_20[i%100 - 1]
                else:
                    str_num += multiple_ten[tens - 2]
                    if units != 0:
                        str_num += under_20[units - 1]      
        letter_sum += len(str_num)
    return letter_sum


if __name__ == '__main__':
    # Check provided test case
    assert 19 == number_letter_count(5)

    # Compute result
    start = time()
    print(number_letter_count(1000))
    print("Execution time: " + str(time() - start))