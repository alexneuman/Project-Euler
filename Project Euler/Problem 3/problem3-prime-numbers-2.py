
from math import sqrt

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


