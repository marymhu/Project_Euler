'''
Smallest Multiple
https://projecteuler.net/problem=5
'''

def smallest_multiple (max_term):
    '''
    Find smallest multiple of numbers between 1 .. max_term
    '''
    value = max_term
    found = False
    while found == False:
        for div in range (max_term, 1, -1):
            found = True
            if value%div != 0:
                found = False
                break
        if found == False:
            value += max_term
    return value
    
if __name__=='__main__':
    print (smallest_multiple(20))