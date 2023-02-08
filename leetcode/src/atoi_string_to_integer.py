"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer
(similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

    Read in and ignore any leading whitespace.
    Check if the next character (if not already at the end of the string) is '-' or '+'.
    Read this character in if it is either. This determines if the final result is negative or positive respectively.
    Assume the result is positive if neither is present.
    Read in next the characters until the next non-digit character or the end of the input is reached.
    The rest of the string is ignored.
    Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
    If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
    If the integer is out of the 32-bit signed integer range [-2**31, 2**31 - 1], then clamp the integer so that it
    remains in the range.
    Specifically, integers less than -2**31 should be clamped to -2**31,
    and integers greater than 2**31 - 1 should be clamped to 2**31 - 1.
    Return the integer as the final result.

Note:
    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

Constraints:
    0 <= s.length <= 200
    s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""
import re


def my_atoi(s: str) -> int:
    res = s.lstrip(' ')
    if not res:
        return 0
    sign = 1
    if res[0] in {'-', '+'}:
        sign = -1 if res[0] == '-' else 1
        res = res[1:]
    if not res or not res[0].isnumeric():
        return 0
    for i in range(len(res)):
        if not res[i].isnumeric():
            res = res[:i]
            break
    return min(max(sign * int(res), -2**31), 2**31 - 1)


def my_atoi1(s: str) -> int:
    res = (
        int(match.group(0))
        if (match := re.match(r"\s*[+-]?\d+", s))
        else 0
    )
    return min(max(res, -2 ** 31), 2 ** 31 - 1)


print(my_atoi("42"))
print(my_atoi("   -42"))
print(my_atoi("4193 with words"))
print(my_atoi1("4193 with words"))
print(my_atoi("   -04f"))
print(my_atoi1("   -04f"))
