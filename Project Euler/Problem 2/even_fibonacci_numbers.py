"""Finds the sum of even fibbonacci numbers whose values do not exceed four million"""

def even_fibs_below_four_million():
    a, b = 0, 1
    while a < 4000000:
        a, b = b, a +  b
        if a % 2 == 0:
            yield a

fibs = even_fibs_below_four_million()
print(sum(fibs))

