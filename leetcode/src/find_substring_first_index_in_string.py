"""
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
Constraints:
    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.
"""


def find_substring_first_index_in_string(haystack: str, needle: str) -> int:
    if needle not in haystack:
        return -1
    l = len(needle)
    for i in range(len(haystack)):
        if haystack[i:i+l] == needle:
            return i


def find_substring_first_index_in_string1(haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.index(needle)
    return -1


def find_substring_first_index_in_string2(haystack: str, needle: str) -> int:
    try:
        return haystack.index(needle)
    except:
        return -1


print(find_substring_first_index_in_string(haystack="sadbutsad", needle="sad"))
print(find_substring_first_index_in_string(haystack="leetcode", needle="leeto"))
