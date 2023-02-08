"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-2**31, 2**31 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Constraints: -2**31 <= x <= 2**31 - 1
"""


def reverse(x: int) -> int:
    op = -1 if x < 0 else 1
    r = list(str(abs(x)))
    r.reverse()
    s = ""
    for char in r:
        s += char
    res = int(s) * op
    if -2 ** 31 <= res <= 2 ** 31 - 1:
        return res
    return 0


def reverse1(x: int) -> int:
    op = -1 if x < 0 else 1
    s = str(abs(x))[::-1]
    res = int(s) * op
    if -2 ** 31 <= res <= 2 ** 31 - 1:
        return res
    return 0


print(reverse1(123))
print(reverse1(-123))
print(reverse1(120))
print(reverse1(5))
print(reverse1(0))
print(reverse1(-8463847412))
print(reverse1(7463847412))
print(reverse1(-9463847412))
print(reverse1(8463847412))
