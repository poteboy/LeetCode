#Runtime: 48 ms, faster than 31.24% of Python3 online submissions for Validate Binary Search Tree.
#Memory Usage: 15.1 MB, less than 100.00% of Python3 online submissions for Validate Binary Search Tree.

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        min = float('inf')
        max = float('-inf')
        return self.check(root, min, max)

    def check(self, root, min, max) ->bool:
        if not root:
            return True
        if root.val > max or root.val < min:
            return False
        leftisTrue = self.check(root.left, min, root.val)
        rightisTrue = self.check(root.right, root.val, max)
        return leftisTrue and rightisTrue
