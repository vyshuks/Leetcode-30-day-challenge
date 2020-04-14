# You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

# direction can be 0 (for left shift) or 1 (for right shift). 
# amount is the amount by which string s is to be shifted.
# A left shift by 1 means remove the first character of s and append it to the end.
# Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
# Return the final string after all operations.


from collections import deque

def stringShift(mystr, shift):
    left_shift = right_shift = 0
    for s in shift:
        if s[0] == 0:
            left_shift += (-1 * s[1])
        else:
            right_shift += (1 * s[1])
    
    final_shift = left_shift + right_shift
    dq = deque(mystr)
    dq.rotate(final_shift)
    return "".join(dq)

print(stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]]))
