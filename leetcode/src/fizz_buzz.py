"""
Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.

Constraints: 1 <= n <= 10**4
"""
from typing import List


def fizz_buzz(n: int) -> List[str]:
    def value(i: int) -> str:
        if i % 3 == 0 and i % 5 == 0:
            return "FizzBuzz"
        elif i % 3 == 0:
            return "Fizz"
        elif i % 5 == 0:
            return "Buzz"
        else:
            return str(i)
    result = []
    for j in range(n):
        result.append(value(j+1))
    return result


def fizz_buzz1(n: int) -> List[str]:
    return ["Fizz"*(i % 3 == 0) + "Buzz"*(i % 5 == 0) or f"{i}" for i in range(1, n+1)]


def fizz_buzz2(n: int) -> List[str]:
    result = []
    for i in range(1, n+1):
        div_by_3 = "Fizz"*(i % 3 == 0)
        div_by_5 = "Buzz"*(i % 5 == 0)
        result.append(div_by_3 + div_by_5 or f"{i}")
    return result


print(fizz_buzz(3), '\n', fizz_buzz1(3), '\n', fizz_buzz2(3))
print(fizz_buzz(5), '\n', fizz_buzz1(5), '\n', fizz_buzz2(5))
print(fizz_buzz(15), '\n', fizz_buzz1(15), '\n', fizz_buzz2(15))
