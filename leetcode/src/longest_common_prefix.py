"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""
from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    prefix = ""
    sorted_strs = sorted(strs, key=lambda s: len(s))
    for i in range(len(sorted_strs[0])):
        present = True
        for j in range(1, len(sorted_strs)):
            if sorted_strs[0][i] != sorted_strs[j][i]:
                present = False
        if not present:
            break
        prefix = prefix + sorted_strs[0][i]
    return prefix


def longest_common_prefix1(strs: List[str]) -> str:
    strs.sort(key=lambda x: len(x))
    prefix = strs[0]
    for i in range(len(strs[0]), 0, -1):
        if all([prefix[:i] == strs[j][:i] for j in range(1, len(strs))]):
            return prefix[:i]
    return ""


def longest_common_prefix2(strs: List[str]) -> str:
    prefix = min(strs, key=len)
    for i, ch in enumerate(prefix):
        for other in strs:
            if other[i] != ch:
                return prefix[:i]
    return prefix


def longest_common_prefix3(strs: List[str]) -> str:
    prefix = min(strs, key=len)
    for i in strs:
        while prefix != i[:len(prefix)]:
            prefix = prefix[:-1]
    return prefix


print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
print(longest_common_prefix(["cir", "car"]))
