"""
Number of Steps to Reduce a Number to Zero

Given an integer num, return the number of steps to reduce it to zero.
In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
Constraints: 0 <= num <= 10**6
"""


def number_of_steps(num: int) -> int:
    n = 0
    while num > 0:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        n += 1
    return n


def number_of_steps1(num: int) -> int:
    return max((num.bit_length() - 1) + num.bit_count(), 0)  # max() used for edge case where num = 0


print(number_of_steps(14))
print(number_of_steps(8))
print(number_of_steps(123))
print(number_of_steps(0))
