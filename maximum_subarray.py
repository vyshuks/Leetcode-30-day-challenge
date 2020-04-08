# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


def maxSubArray(nums: List[int]) -> int:
    max_ending = 0
    max_so_far = None
    for num in nums:
        max_ending = max_ending + num
        if max_so_far is None:
            max_so_far = max_ending
        else:
            max_so_far = max(max_ending, max_so_far)
        max_ending = max(max_ending, 0)

    return max_so_far

print(maxSubArray([-2, -1]))