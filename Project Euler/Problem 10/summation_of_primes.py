"""This program finds all prime numbers below two million"""

from math import sqrt

def is_prime(n):
	return all(n % i != 0 for i in range(2, int(sqrt(n))+1))
	
def get_primes(num=2000000):
	primes = []
	for n in range(2, num):
		if is_prime(n):
			primes.append(n)
	return sum(primes)
			
print(get_primes())