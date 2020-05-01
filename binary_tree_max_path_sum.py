"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes
from some starting node to any node in the tree along the
parent-child connections. The path must contain at least
one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root):
    m = {'max_num': None}
    path_sum(root, m)
    return m.get('max_num', 0)

def path_sum(node, max_num):
    print("*******")
    print(node)
    if not node:
        return 0

    left = max(0, path_sum(node.left, max_num))
    right = max(0, path_sum(node.right, max_num))
    if max_num.get('max_num'):
        max_num['max_num'] = max(max_num['max_num'], (left+right+node.val))
    else:
        max_num['max_num'] = left+right+node.val
    return max(left,right) + node.val

t1 = TreeNode()
t1.val = 1
t1.left = 2
t1.right = 3
print(max_path_sum(t1))