"""This program finds the single pythagorean triplet for which a + b +c = 1000"""

from math import sqrt
from functools import reduce

TOTAL = 1000

def get_pyt():
	for a in range(1, int(TOTAL)):
		for b in range(1, int(TOTAL)):
			c = TOTAL - a - b
			if a**2 + b**2 == c**2:
				return reduce(lambda x, y: x*y, (a, b, c))
			
print(get_pyt())