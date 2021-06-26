"""A program which calculates largest primes of an integer in O(log n) time.
"""
from math import sqrt

cheap_count = 0
total_cheap = 0
expensive_count = 0
total_expensive = 0

def is_prime(num: int) -> bool:
	"""Returns whether integer is prime"""
	count = 0
	
	for i in range(2, int(sqrt(num))):
		if num % i == 0:
			break
		count += 1
	
	if count/s >= .5:
		global expensive_count
		global total_expensive
		expensive_count += 1
		total_expensive += count
		
	elif count/s <= .5:
		global cheap_count
		global total_cheap
		cheap_count += 1
		total_cheap += count

	return all(num % i != 0 for i in range(2, int(sqrt(num)+ 1)))

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

s = perf_counter()
for i in range(20000000000, 20000005000):
	start = perf_counter()
	p = get_prime(i)
	end = perf_counter()
	time = end - start
f = perf_counter()
print(f - s)
print(f'Num expensive is {expensive_count}, num cheap is {cheap_count} \n, the average size of a cheap call is {total_cheap/cheap_count}, the average size of an expensive call is {total_expensive/expensive_count}')