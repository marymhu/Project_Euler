'''
Sum square difference
https://projecteuler.net/problem=6
'''

def sum_square (max_term):
    '''
    Sum of the squares of the first max_term natural numbers
    '''
    sum = 0
    for i in range(1, max_term+1):
        sum += i*i
    return sum
    
def square_sum (max_term):
    '''
    Square of the sum of the first max_term natural numbers
    '''
    sum = 0
    for i in range(1, max_term+1):
        sum += i
    return sum*sum
    
if __name__=='__main__':
    print (str(square_sum(100) - sum_square(100)))