# Given an integer array arr, count element x such that x + 1 is also in arr.

# If there're duplicates in arr, count them seperately.

 

# Example 1:

# Input: arr = [1,2,3]
# Output: 2
# Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
# Example 2:

# Input: arr = [1,1,3,3,5,5,7,7]
# Output: 0
# Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.
# Example 3:

# Input: arr = [1,3,2,3,5,0]
# Output: 3
# Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.
# Example 4:

# Input: arr = [1,1,2,2]
# Output: 2
# Explanation: Two 1s are counted cause 2 is in arr.


def count_elements(arr):
    d = {}
    for i in arr:
        d[i] = 1

    count = 0
    for num in arr:
        num_plus = num + 1
        if num_plus in d:
            count += 1
        
    return count

print(count_elements([1,1,2,2]))