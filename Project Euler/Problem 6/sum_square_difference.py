"""A program that calculates the difference between the sum of squares of a range of numbers and the square of the sum"""

from functools import reduce

def sum_squares(num):
	return sum(n**2 for n in range(1, num+1))

def squared_sum_of_range(num):
	return reduce(lambda f, s: f+s, range(1, num+1)) ** 2

def get_sum_square_difference(num):
	return squared_sum_of_range(num) - sum_squares(num)

print(get_sum_square_difference(100))