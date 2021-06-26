"""A program that comutes the nth prime number"""

from math import sqrt

def is_prime(n):
	return all(n % i != 0 for i in range(2, int(sqrt(n) +1)))

def count_primes(nth_prime):
	num = 1
	primes_count = 1 #starts at 1 to account for prime 2
	while True:
		num += 2
		if is_prime(num):
			primes_count += 1
			if primes_count == nth_prime:
				print(f'{num} is the #{primes_count} prime')
				return num

count_primes(10001)