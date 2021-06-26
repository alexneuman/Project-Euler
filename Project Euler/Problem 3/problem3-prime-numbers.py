"""A program which calculates largest primes of an integer in O(log n) time.
"""
from math import sqrt

def is_prime(num: int) -> bool:
	"""Returns whether integer is prime"""
	for i in range(2, int(sqrt(num)+ 1)):
		if num % i == 0:
			return False
	return True

def get_prime(n: int, _start: bool=True) -> int:
	"""Calculates largest factor of  `n`.
		Parameter `end` is flag used to signal recursion.
	"""
	max_prime = 0
	
	if is_prime(n):
		if n > max_prime:
			max_prime = n
		return max_prime # break recursion
	
	for i in range(2, n):
			if n % i == 0: #match
				n //= i
				return get_prime(n, _start=False) #recursively pulls out subfactors, ex: 68 -> 34 & 2 -> 17
				
	return max_prime

from time import perf_counter

#For measuring the time-cost of calculating different numbers
s = perf_counter()
for i in range(1, 10000):
	start = perf_counter()
	p = get_prime(i)
	end = perf_counter()
	time = end - start
	#print(f'number={i}, max_prime={p}, time={time}')
f = perf_counter()
print(f - s)

