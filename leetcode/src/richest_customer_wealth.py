"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money
the i-th customer has in the j-th bank. Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts.
The richest customer is the customer that has the maximum wealth.
Constraints:
    m == accounts.length
    n == accounts[i].length
    1 <= m, n <= 50
    1 <= accounts[i][j] <= 100
"""
from typing import List


def maximum_wealth(accounts: List[List[int]]) -> int:
    return max(sum(i) for i in accounts)


def maximum_wealth1(accounts: List[List[int]]) -> int:
    return max(map(sum, accounts))


print(maximum_wealth([[1,2,3],[3,2,1]]))
print(maximum_wealth([[1,5],[7,3],[3,5]]))
print(maximum_wealth([[2,8,7],[7,1,3],[1,9,5]]))
