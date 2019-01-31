'''
Sum of even-valued Fibonacci terms under 4_000_000 
https://projecteuler.net/problem=2
'''

def Fibonacci (max_val):
    fib_list = [1,2]
    new_term = 0
    while new_term < max_val:
        new_term = sum(fib_list[-2:])
        if new_term < max_val:
            fib_list.append(sum(fib_list[-2:]))
    # Reducing Fibonacci terms list to even values
    fib_even = [val for val in fib_list if val%2 == 0]
    return sum(fib_even)

if __name__=='__main__':
    print (Fibonacci (4000000))