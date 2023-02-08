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

Given a roman numeral, convert it to an integer.
"""


def roman_to_int(s: str) -> int:
    translation = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    symbols = list(translation.keys())
    symbols.reverse()
    string = list(s)
    result = 0
    for symbol in symbols:
        if symbol in string:
            for i in range(string.count(symbol)):
                index = string.index(symbol)
                if index > 0 and string[index-1] in symbols[symbols.index(symbol)+1:]:
                    result += translation[string[index]]
                    result -= translation[string[index-1]]
                    string.pop(index-1)
                    string.pop(index-1)
                else:
                    result += translation[string[index]]
                    string.pop(index)
    return result


def roman_to_int0(s: str) -> int:
    translation = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    symbols = list(translation.keys())
    symbols.reverse()
    result = 0
    for symbol in symbols:
        if symbol in s:
            for i in range(s.count(symbol)):
                index = s.index(symbol)
                if index > 0 and s[index-1] in symbols[symbols.index(symbol)+1:]:
                    result += translation[s[index]]
                    result -= translation[s[index-1]]
                    s = s.replace(s[index-1], '', 1)
                    s = s.replace(s[index-1], '', 1)
                else:
                    result += translation[s[index]]
                    s = s.replace(s[index], '', 1)
    return result


def roman_to_int1(s: str) -> int:
    translation = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s) - 1):
        if translation[s[i]] < translation[s[i + 1]]:
            result -= translation[s[i]]
        else:
            result += translation[s[i]]
    return result + translation[s[-1]]


def roman_to_int2(s: str) -> int:
    translation = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
                   "IV": -2, "IX": -2, "XL": -20, "XC": -20, "CD": -200, "CM": -200}
    result = 0
    for symbol, quantity in translation.items():
        result += s.count(symbol) * quantity
    return result


def roman_to_int3(s: str) -> int:
    translation = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX")\
        .replace("CD", "CCCC").replace("CM", "DCCCC")
    for symbol in s:
        result += translation[symbol]
    return result


def roman_to_int4(s: str) -> int:
    translation = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX")\
        .replace("CD", "CCCC").replace("CM", "DCCCC")
    return sum(map(lambda x: translation[x], s))


print(str(roman_to_int("III"))+'\t'+str(roman_to_int0("III"))+'\t'+str(roman_to_int4("III")))
print(str(roman_to_int("LVIII"))+'\t'+str(roman_to_int0("LVIII"))+'\t'+str(roman_to_int4("LVIII")))
print(str(roman_to_int("XLVIII"))+'\t'+str(roman_to_int0("XLVIII"))+'\t'+str(roman_to_int4("XLVIII")))
print(str(roman_to_int("MCMXCIV"))+'\t'+str(roman_to_int0("MCMXCIV"))+'\t'+str(roman_to_int4("MCMXCIV")))
print(str(roman_to_int("MMMCMXCIX"))+'\t'+str(roman_to_int0("MMMCMXCIX"))+'\t'+str(roman_to_int4("MMMCMXCIX")))
