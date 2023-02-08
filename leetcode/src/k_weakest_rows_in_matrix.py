"""
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians).
The soldiers are positioned in front of the civilians.
That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:
    - The number of soldiers in row i is less than the number of soldiers in row j.
    - Both rows have the same number of soldiers and i < j.

Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

Constraints:
    m == mat.length
    n == mat[i].length
    2 <= n, m <= 100
    1 <= k <= m
    matrix[i][j] is either 0 or 1.
"""
from typing import List


def k_weakest_rows(mat: List[List[int]], k: int) -> List[int]:
    d = []
    result = []
    for i, value in enumerate(mat):
        d.append(value)
    mat.sort()
    for i in range(k):
        idx = d.index(mat[i])
        result.append(idx)
        d[idx] = 0
    return result


def k_weakest_rows1(mat: List[List[int]], k: int) -> List[int]:
    d = {}
    result = []
    for i, value in enumerate(mat):
        d[i] = value
    mat.sort()
    for i in range(k):
        for index, value in d.items():
            if value == mat[i]:
                result.append(index)
                d[index] = 0
                break
    return result


def k_weakest_rows2(mat: List[List[int]], k: int) -> List[int]:
    m = len(mat)
    rows = sorted(range(m), key=lambda i: (mat[i], i))
    del rows[k:]
    return rows


mat1 = [[1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1]]
k1 = 3
print(k_weakest_rows2(mat1, k1))
print(k_weakest_rows(mat1, k1))

mat2 = [[1, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 0]]
k2 = 2
print(k_weakest_rows2(mat2, k2))
print(k_weakest_rows(mat2, k2))
