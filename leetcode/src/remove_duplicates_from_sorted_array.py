"""
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that
each unique element appears only once. The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, you must instead have
the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates, then the first k elements of nums
should hold the final result. It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.
Constraints:
    1 <= nums.length <= 3 * 104
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.
"""
from typing import List


def remove_duplicates(nums: List[int]) -> int:
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


def remove_duplicates1(nums: List[int]) -> int:
    nums[:] = sorted(set(nums))
    return len(nums)


l = [1,1,2]
print(remove_duplicates(l))
print(l)

l = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates(l))
print(l)
