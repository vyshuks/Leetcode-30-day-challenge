We have a collection of stones, each stone has a positive integer weight.

# Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

# Example 1:

# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.


import heapq

def last_stone_weight(arr):

    if len(arr) == 0:
        return 0
    if len(arr) ==  1:
        return arr[0]

    new_arr = []
    for num in arr:
        new_arr.append(-1 * num)
    heapq.heapify(new_arr)

    while True:
        
        w1 = -1 * heapq.heappop(new_arr)
        w2 = -1 * heapq.heappop(new_arr)
        if w1==w2:
            
            if len(new_arr) == 0:
                return 0
            
        else:
            new_weight = w1-w2
            heapq.heappush(new_arr, -1 * new_weight)
            

        if len(new_arr) == 1:
            return -1 * new_arr[0]


print(last_stone_weight([2,7,4,1,8,1]))
