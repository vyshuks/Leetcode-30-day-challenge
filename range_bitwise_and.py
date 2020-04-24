"""
Given a range [m, n] where 0 <= m <= n <= 2147483647,
return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
"""
def msb(num):
    """
    Return most significant
    bit
    :param num: int
    :return: int
    """
    val = -1
    while num > 0:
        num = num >> 1
        val += 1
    return val

def bitwiseand_range(m, n):
    """
    calculate bitwise range AND
    :param m: int
    :param n: int
    :return: int
    """
    result = 0
    while m > 0 and n > 0:
        msb_m = msb(m)
        msb_n = msb(n)
        if msb_m != msb_n:
            break
        msb_val = (1<<msb_m)
        result += msb_val

        m = m - msb_val
        n = n - msb_val

    return result

print(bitwiseand_range(0,1))