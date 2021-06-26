"""A program that computes the lowest common factor of a range of integers. Not optimized for prime values.
Can optionally use cached values."""

from math import sqrt
from operator import mul
import pickle
import os

CACHE = True

if os.path.exists('found_3.p') and CACHE:
	emp = open('found_3.p', 'rb')
	found_values = pickle.load(emp)
else:
	found_values = {}
	
def incrementor(num: int) -> int:
	"""Finds the lowest common factor of a value over a given range of values
		This incrementor is slow for odd numbers
	"""
	print('Attempting to get inc for', num)
	mul = 1
	original = num
	is_prime = lambda x: all(x % i != 0 for i in range(2, int(sqrt(x) + 1)))

	while num > 7 and not is_prime(num): #
		for div in (7, 5, 4, 3, 2):
			if num % div == 0:
				num //= div
				mul *= div
	 
	for n in range(2, original): #compresses into a smaller factor
		if original % n == 0:
			original //= n
			break
	
	i = 1
	while True: #finds the smallest common factor to that number
		i += 1
		if all(i % j == 0 for j in range(2, original)):
			break	
	return i * mul
	
def get_prev(num):
	"""Attempts to find common factor by using previously found values"""
	print('Trying to cache for', num)
	if num % 2 != 0:
		if found_values[num - 1] % num == 0:
			prev_value = found_values[num-1]
		else:
			return None
	else:
		print('Using prev values... ')
		prev_value = found_values[num - 2]
	return prev_value

def calc_lcm(num: int):
	
	inc = None
	if num != 2:
		inc = get_prev(num) #if perfectly divisible	
	if not inc: #brute force, much slower
		inc = incrementor(num)
	
	count = 0
	while True:
		count += inc
		if all(count % i == 0 for i in range(2, num + 1)):
			found_values[num] = count
			if CACHE:
				pickle.dump(found_values, open('found_3.p', 'wb'))
			break		
	return count

def lcm(num):
	"""Finds and returns the lcm of a given number"""
	
	if CACHE:
		if found_values.get(num):
			print(f'Using cache for: {num} ')
			return found_values[num]
	try:
		start = max(found_values)
	except:
		start = 2
	
	for n in range(start, num + 1):
		print(calc_lcm(n))
	return found_values[num]

#print(incrementor(5))
print(lcm(23))

#from time import perf_counter
#s = perf_counter()
#print(find_lowest(4))
#f = perf_counter()
#print(f - s)
#print('Second pickle', found_values)