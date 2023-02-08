"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters
from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Constraints:
    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.
"""
from collections import Counter


def can_construct(ransomNote: str, magazine: str) -> bool:
    for char in ransomNote:
        if char not in magazine:
            return False
        magazine = magazine.replace(char, '', 1)
    return True


def can_construct1(ransomNote: str, magazine: str) -> bool:
    ransomNoteCount = Counter(ransomNote)
    magazineCount = Counter(magazine)
    for c in ransomNoteCount:
        if c not in magazineCount or ransomNoteCount[c] > magazineCount[c]:
            return False
    return True


def can_construct2(ransomNote: str, magazine: str) -> bool:
    st1, st2 = Counter(ransomNote), Counter(magazine)
    return st1 & st2 == st1


def can_construct3(ransomNote: str, magazine: str) -> bool:
    st1, st2 = Counter(ransomNote), Counter(magazine)
    return st1 <= st2


print(can_construct(ransomNote="a", magazine="b"))
print(can_construct(ransomNote="aa", magazine="ab"))
print(can_construct(ransomNote="aa", magazine="aab"))
