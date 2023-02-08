"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
Constraints:
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -10**6 <= nums1[i], nums2[i] <= 10**6
"""
from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    len1, len2 = len(nums1), len(nums2)
    length = (len1 + len2) // 2
    if length == 0:
        if len1 == 0 and len2 == 0:
            return 0
        elif len1 == 0:
            return nums2[0]
        else:
            return nums1[0]
    i = j = value1 = value2 = 0
    for k in range(length + 1):
        if i < len1 and j < len2:
            if nums1[i] <= nums2[j]:
                value1 = nums1[i]
                i += 1
            else:
                value1 = nums2[j]
                j += 1
        elif i < len1:
            value1 = nums1[i]
            i += 1
        elif j < len2:
            value1 = nums2[j]
            j += 1
        if k == length - 1:
            value2 = value1
    if (len1 + len2) % 2 == 0:
        return float((value1 + value2) / 2)
    return value1


def find_median_sorted_arrays1(nums1: List[int], nums2: List[int]) -> float:
    n1 = len(nums1)
    n2 = len(nums2)
    if n1 > n2:
        return find_median_sorted_arrays1(nums2, nums1)  # WE SHALL DO BINARY SEARCH ON THE SMALLER ARRAY, NUMS1

    INT_MIN, INT_MAX = -2 ** 64, 2 ** 64  # SETUP INT_MIN AND INT_MAX FOR EMPTY LEFT / RIGHT PARTITION
    low = 0
    high = n1  # pointers for BINARY SEARCH ON THE SMALLER ARRAY NUMS1

    while low <= high:
        # GET THE PARTITIONS POINTS OF BOTH ARRAYS
        cut1 = (low + high) // 2  # partition of nums1
        cut2 = (n1 + n2 + 1) // 2 - cut1  # partition of nums2

        # GET THE 4 BOUNDARY NUMBERS
        left1 = nums1[cut1 - 1] if cut1 > 0 else INT_MIN  # left1 is the left partition of cut1
        right1 = nums1[cut1] if cut1 < n1 else INT_MAX  # right1 is the right partition of cut1

        left2 = nums2[cut2 - 1] if cut2 > 0 else INT_MIN  # left2 is the left partition of cut2
        right2 = nums2[cut2] if cut2 < n2 else INT_MAX  # right2 is the right partition of cut2

        # CORRECT PARTITION FOUND
        if left1 <= right2 and left2 <= right1:  # Got the Answer => Median
            if (n1 + n2) % 2 == 0:
                return (max(left1, left2) + min(right1, right2)) / 2
            else:
                return max(left1, left2)

        # MOVE cut1 (mid of binary search) LEFTWARDS
        elif left1 > right2:
            high = cut1 - 1

        # MOVE cut1 (mid of binary search) RIGHTWARDS
        else:
            low = cut1 + 1

    return 0.0  # For both empty arrays


print(find_median_sorted_arrays(nums1=[1, 3], nums2=[2]))
print(find_median_sorted_arrays1(nums1=[1, 3], nums2=[2]))
print(find_median_sorted_arrays(nums1=[1, 2], nums2=[3, 4]))
print(find_median_sorted_arrays1(nums1=[1, 2], nums2=[3, 4]))
print(find_median_sorted_arrays(nums1=[], nums2=[3, 4]))
print(find_median_sorted_arrays1(nums1=[], nums2=[3, 4]))
print(find_median_sorted_arrays(nums1=[], nums2=[3]))
print(find_median_sorted_arrays1(nums1=[], nums2=[3]))
print(find_median_sorted_arrays(nums1=[], nums2=[]))
print(find_median_sorted_arrays1(nums1=[], nums2=[]))
