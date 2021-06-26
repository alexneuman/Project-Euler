"""A program that finds the largest product of 13 sequential numbers in a given array"""

from num_grid import grid
from itertools import islice
from functools import reduce
from collections import deque

mul = lambda x, y: x*y

current = deque(islice(grid, 13), 13)
best_product = reduce(mul, current)
best_combo = []

for nums in grid:
	current.appendleft(nums)
	get_product = reduce(mul, current)
	if get_product > best_product:
		print(best_product, best_combo)
		best_product = get_product
		best_combo = current

print(best_product, best_combo)