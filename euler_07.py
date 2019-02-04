'''
10001st prime
https://projecteuler.net/problem=7
'''

def compute_prime (nth):
    '''
    Compute the nth prime number
    '''
    prime_list = [2, 3]
    cur_val = prime_list [-1]
    while len(prime_list) < nth:
        cur_val += 2
        is_prime = True
        for p in prime_list:
            if cur_val%p == 0:
                is_prime = False
        if is_prime:
            prime_list.append(cur_val)
    return prime_list[-1]
    
if __name__=='__main__':
    assert 13 == compute_prime(6), "Error while computing 6th prime"
    print(compute_prime(10001))