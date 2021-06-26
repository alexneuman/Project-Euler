"""Finds largest palindrome (a number which reads the same both ways) of two given numbers"""

def is_palindrome(n):
    if ''.join(reversed(str(n))) == str(n):
        return True
    return False

def get_palindromes(digits_1: int, digits_2: int):
    max_palindrome = 0
    mults = None
    mult_1 = 10**digits_1
    mult_2 = 10**digits_2

    for m1 in reversed(range(mult_1//10, mult_1)):
        for m2 in reversed(range(mult_2//10, mult_2)):
            if is_palindrome(m1*m2):
                if m1* m2 > max_palindrome:
                    max_palindrome = m1 * m2
                    mults = m1, m2
    return max_palindrome, mults

print(get_palindromes(3, 3))