# is_prime(n): returns True if n is a prime number, False otherwise
# print_primes(n): prints all prime numbers less than n
# get_primes(n): returns a list of all prime numbers less than n
# test in scratch paper ipynb

def is_prime(n):
    for i in range(2, n):  # excluding 1 and the n number itself 
        if n % i == 0:
            return False
    return True 

def print_primes(n):
    for j in range(1, n):
        if is_prime(j):
            print(j, end = " ")
    
def get_primes(n): 
    prime = []
    for j in range(1, n):
        if is_prime(j):
            prime.append(j)
    return prime
    