"""
Given an array of integers and an integer k, you need to find the
total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

def sub_array_sum(nums, k):
    """
    Find sub array sum
    :param nums: list of number
    :param k: key to find
    :return: int
    """
    total = 0
    result = 0
    list_total = {0: 1}

    for num in nums:
        total += num

        if list_total.get(total-k):
            result += list_total.get(total-k)
        list_total[total] = list_total.get(total, 0) + 1
    return result

print(sub_array_sum([0,0,0,0,0,0,0,0,0,0], 0))
