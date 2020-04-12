
Runtime: 28 ms, faster than 65.82% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 13.7 MB, less than 5.72% of Python3 online submissions for Binary Tree Postorder Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        curr = []
        return self.helper(root, curr)
        
    def helper(self, root, curr):
        if root:
            self.helper(root.left, curr)
            self.helper(root.right, curr)
            curr.append(root.val)
        return curr
        
