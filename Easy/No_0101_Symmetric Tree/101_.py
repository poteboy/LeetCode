#Runtime: 36 ms, faster than 35.89% of Python3 online submissions for Symmetric Tree.
#Memory Usage: 13.9 MB, less than 5.17% of Python3 online submissions for Symmetric Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.helper(root, root)
        
    def helper(self, A, B):
        if not A and not B:
            return True
        elif not A or not B:
            return False
        return A.val == B.val and self.helper(A.left, B.right) and self.helper(A.right, B.left)
