'''
Largest palindrome product
https://projecteuler.net/problem=4
'''

def is_palindrome (value):
    str_val = str(value)
    for idx, digit in enumerate(str_val[0:int(len(str_val)/2)+1]):
        if digit != str_val[len(str_val) - idx - 1]:
            return False
    return True

def largest_palindrome (digits):
    largest_val = 0
    # Testing largest products first
    max_val = 10**(digits) - 1
    min_val = 10**(digits - 1)
    
    for i in range (max_val, min_val, -1):
        for j in range (i, min_val, -1):
            tested_val = i*j
            if is_palindrome (tested_val) and tested_val > largest_val:
                largest_val = tested_val
    return largest_val
    
if __name__=='__main__':
    print (largest_palindrome (3))