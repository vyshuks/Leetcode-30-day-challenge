"""
Given a binary tree where each path going from the root to any
leaf form a valid sequence, check if a given string is a valid
sequence in such binary tree.

We get the given string from the concatenation of an array of
integers arr and the concatenation of all values of the nodes
along a path results in a sequence in the given binary tree.


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        arr_len = len(arr)

        def is_leaf(node):
            return node.left is None and node.right is None

        def dfs(node, index):
            if index == arr_len - 1:
                if node is not None and arr[index] == node.val:
                    return is_leaf(node)
                return False
            if node is None:
                return False
            if node.val == arr[index]:
                return dfs(node.left, index + 1) or dfs(node.right, index + 1)
            return False

        return dfs(root, 0)