# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.
# Example 1:
# Input: "()"
# Output: True
# Example 2:
# Input: "(*)"
# Output: True
# Example 3:
# Input: "(*))"
# Output: True


def checkValidString(s):
    low = 0
    high = 0
    for c in s:
        if c == "(":
            low += 1
            high += 1
        elif c == ")":
            low -= 1
            high -= 1
        elif c == "*":
            low -= 1
            high += 1
        low = max(low, 0)
        if(high < 0):
            return False 
    return low == 0


print(checkValidString("*"))