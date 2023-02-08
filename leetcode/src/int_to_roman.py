"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.
Constraints: 1 <= num <= 3999
"""


def int_to_roman(num: int) -> str:
    # translation = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # reverse_translation = dict(zip(translation.values(), translation.keys()))
    reverse_translation = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    result = ""
    number = str(num)
    for i in range(len(number)):
        n = int(number[i])
        exp = 10**(len(number)-i-1)
        if n == 9:
            result += reverse_translation[exp] + reverse_translation[exp * 10]
        elif n in {5, 6, 7, 8}:
            result += reverse_translation[exp * 5] + reverse_translation[exp] * (n-5)
        elif n == 4:
            result += reverse_translation[exp] + reverse_translation[exp * 5]
        else:
            result += reverse_translation[exp] * n
    return result


roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
         100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
         10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}


def int_to_roman1(num: int) -> str:
    result = ""
    for i in roman.keys():
        while num >= i:
            num -= i
            result += roman[i]
    return result


def int_to_roman2(num: int) -> str:
    result = ""
    for key, value in roman.items():
        result += value * (num // key)
        num %= key
    return result


print(int_to_roman(3), '\t', int_to_roman2(3))
print(int_to_roman(58), '\t', int_to_roman2(58))
print(int_to_roman(48), '\t', int_to_roman2(48))
print(int_to_roman(1994), '\t', int_to_roman2(1994))
print(int_to_roman(3999), '\t', int_to_roman2(3999))
print(int_to_roman(999), '\t', int_to_roman2(999))
