from numbers_grid import numbers
from functools import reduce
from math import floor
import numpy as np

class Grid:
	ROW_SIZE = 20
	COL_SIZE = 20
	TOTAL_IN_GRID = ROW_SIZE * COL_SIZE
	print(np.array(numbers).reshape(ROW_SIZE, COL_SIZE))
	
	def __init__(self):
		self.col = 1
		self.row = 1
		self.max_product = 0
		self.max_combination = None
		self.max_location = None
		self.direction_of_max = None
		
	def validate_rows_cols(self) -> None:
		"""Validator for row and column lengths"""
		if self.col < 1 or self.row < 1:
			raise ValueError('Col and row must be positive.')
		if self.col > 21 or self.row > 20:
			raise ValueError('Col and row cannot be greater than 20')
	
	def calc_product(self, values: int, direction: str) -> None:
		"""Calculates the product of up to four values in a row. Sets highest product if larger than previous."""
		
		if len(values) > 1:
			product = reduce(lambda x, y: x*y, values)
		else:
			product = values[0]
		if product > self.max_product or self.max_product is None:
			self.max_product = product
			self.max_combination = tuple(values)
			self.max_location = (self.col, self.row)
			self.direction_of_max = direction
		
	def check_left_diag(self):
		if (self.col == 1 or self.row == 20):
			nums_in_line = 1
		elif (self.col == 2 and self.row == 17) or (self.col in range(1,21) and self.row == 19):
			nums_in_line = 2
		elif (self.col == 3 and self.row == 16) or self.row == 3 or self.row == 18:
			nums_in_line = 3
		else:
			nums_in_line = 4

		values = [numbers[self.start + i*19 - 1] for i in range(nums_in_line)]
		self.calc_product(values, direction='Left Diagonal')
		
	def check_right_diag(self):
		self.validate_rows_cols()
		if self.col == 20 or self.row == 20:
			nums_in_line = 1
		elif (self.col == 19 and self.row != 20) or (self.row == 19 and self.col != 20):
			nums_in_line = 2
		elif self.col == 18 or self.row == 18:
			nums_in_line = 3
		else:
			nums_in_line = 4
	
		values = [numbers[self.start + i*21 - 1] for i in range(nums_in_line)]
		self.calc_product(values, direction='Right Diagonal')
	
	def check_across(self):
		self.validate_rows_cols()
		r_length = 20 - self.col % 20 + 1
		if r_length > 4:
			nums_in_line = 4
		elif r_length > 20:
			nums_in_line = 1
		else:
			nums_in_line = r_length 
			
		end = self.row * 20
		if end == self.start:
			values = [numbers[self.start -1]]
		else:
			values = numbers[self.start -1: self.start + nums_in_line -1]
	
		self.calc_product(values, direction='Across')
		
	def check_down(self):
		self.validate_rows_cols()
		if self.row <= 17:
			nums_in_line = 4
		elif self.row == 18:
			nums_in_line = 3
		elif self.row == 19:
			nums_in_line = 2
		elif self.row == 20:
			nums_in_line = 1
	
		if nums_in_line == 1:
			values = [numbers[self.start-1]]
		else:
			values = [numbers[self.start - 1 + i*20] for i in range(nums_in_line)]
		self.calc_product(values, direction='Down')
		
	def get_products(self) -> None:
		"""Iterates through each of the fields and assigns the current row and column"""
		for i, num in enumerate(numbers):
			self.row = floor(i/20) + 1
			self.col = i % 20 + 1
			if num == 0:
				continue
			self.check_right_diag()
			self.check_left_diag()
			self.check_across()
			self.check_down()
		
	@property
	def start(self) -> int:
		"""Calculates the starting index of a given row and column"""
		return self.row * 20 - 20 + self.col
		
	@property
	def result(self) -> str:
		"""Returns final results. It will calculate the values of the grid if it has not been done already"""
		if self.max_product == 0:
			self.get_products()
			
		return f'\n Maximum Product={self.max_product}, location={self.max_location}, direction={self.direction_of_max}, combination={self.max_combination}'

g = Grid()
print(g.result)