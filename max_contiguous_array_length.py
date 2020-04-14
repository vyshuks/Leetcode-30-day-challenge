# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


def findMaxLength(nums: List[int]) -> int:
    s = 0
    max_length = 0
    d = {}
    for i, num in enumerate(nums):
        num = -1 if num == 0 else 1
        s = s + num
        if s == 0:
            max_length = i + 1
        if s in d:
            if max_length < (i - d[s]):
                max_length = (i-d[s])
        else:
            d[s] = i
    return max_length

print(findMaxLength([0,1]))