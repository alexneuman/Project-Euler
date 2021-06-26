"""A program that finds the sums of given multiples below a given number
"""

def get_multiples(n1, n2, limit = 10) -> int:
    mults = []
    for i in range(2, limit):
        if (i % n1 == 0) or (i % n2 == 0):
            mults.append(i)
    return sum(mults)

print(get_multiples(3, 5, 1000))