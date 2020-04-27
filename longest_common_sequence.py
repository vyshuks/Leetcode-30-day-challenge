"""
Given two strings text1 and text2, return the length of their
longest common subsequence.

A subsequence of a string is a new string generated from the
original string with some characters(can be none) deleted without
changing the relative order of the remaining characters. (eg, "ace"
is a subsequence of "abcde" while "aec" is not). A common subsequence
of two strings is a subsequence that is common to both strings.



If there is no common subsequence, return 0.



Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
"""

def longest_sub_seq(text1, text2):
    """
    Return longest sub sequence
    :param text1: str
    :param text2: str
    :return: int
    """
    _m = len(text1)
    _n = len(text2)
    _l = [[0 for _ in range(_n+1)] for _ in range(_m+1)]
    for i in range(_m+1):
        for j in range(_n+1):
            if i == 0 or j == 0:
                _l[i][j] = 0
            elif text1[i-1] == text2[j-1]:
                _l[i][j] = _l[i-1][j-1] + 1
            else:
                _l[i][j] = max(_l[i-1][j], _l[i][j-1])
    return _l[_m][_n]

print(longest_sub_seq("abcde", "ace"))
