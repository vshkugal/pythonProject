"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
could represent. Return the answer in any order.
A mapping of digits to letters is just like on the telephone buttons. Note that 1 does not map to any letters.
Constraints:
    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].
"""
from itertools import product
from typing import List


def letter_combinations(digits: str) -> List[str]:
    if digits == "":
        return []
    phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    combinations = []
    for char in digits:
        combinations.append(list(phone[char]))
    combinations.reverse()
    result = combinations[0]
    for i in range(1, len(combinations)):
        tmp_res = []
        for char in combinations[i]:
            for line in result:
                tmp_res.append(char+line)
        result = tmp_res
    return result


# ------------------------------------------------------------------------------------------------------------
def letter_combinations1(digits: str) -> List[str]:
    if len(digits) == 0:
        return []
    phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    result = ['']
    for d in digits:
        tmp_res = []
        for char in phone[d]:
            tmp_res.extend([line + char for line in result])
        result = tmp_res
    return result


# Using "PRODUCT" from "ITERTOOLS"
def letter_combinations2(digits: str) -> List[str]:
    digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    # step 1: map digits to characters
    chars = [digit_map[digit] for digit in digits]
    # step 2: obtain all possible combinations
    combs = product(*chars)  # or product(chrs for chrs in chars)
    result = []
    for comb in combs:
        if not comb:
            continue
        # step 3: concatenate characters
        string = ''.join(comb)
        # step 4: add to result list
        result.append(string)
    return result


# One-liner Implementation
def letter_combinations3(digits: str) -> List[str]:
    return list(map(''.join, product(
        *({'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}[digit] for
          digit in digits)))) if digits else []


# Backtracking approach
def letter_combinations4(digits: str) -> List[str]:
    if not digits: return []
    phone = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
    result = []

    def dfs(seq, current):  # given sequence of digits, generate combination
        if not seq:  # if sequence become empty,
            result.append(current)  # - append the current combination
            return

        for letter in phone[seq[0]]:  # for each letter in first-digit-letters
            dfs(seq[1:], current + letter)  # - merge letter with current comb, then repeat for next digits

    dfs(digits, "")  # start with full sequence and empty combination
    return result


print(letter_combinations("23"))
print(letter_combinations1("23"))
print(letter_combinations(""))
print(letter_combinations1(""))
print(letter_combinations("2"))
print(letter_combinations1("2"))
