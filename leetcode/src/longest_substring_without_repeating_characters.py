"""
Given a string s, find the length of the longest substring without repeating characters.
Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""


def length_of_longest_substring(s: str) -> int:
    sets = []
    for i in range(len(s)):
        a = set(s[i])
        for j in range(i+1, len(s)):
            if s[j] not in a:
                a.add(s[j])
            else:
                break
        sets.append(a)
    return max(len(i) for i in sets)


def length_of_longest_substring1(s: str) -> int:
    lmax = 0
    for i in range(len(s)):
        a = set(s[i])
        for j in range(i+1, len(s)):
            if s[j] not in a:
                a.add(s[j])
            else:
                break
        if len(a) > lmax:
            lmax = len(a)
    return lmax


print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring("bbbbb"))
print(length_of_longest_substring("pwwkew"))

print(length_of_longest_substring1("abcabcbb"))
print(length_of_longest_substring1("bbbbb"))
print(length_of_longest_substring1("pwwkew"))
