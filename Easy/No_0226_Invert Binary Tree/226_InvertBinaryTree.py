#Runtime: 32 ms, faster than 27.51% of Python3 online submissions for Invert Binary Tree.
#Memory Usage: 13.8 MB, less than 5.41% of Python3 online submissions for Invert Binary Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
'''
            4
           / \
          2   7
         / \ / \
        1  36   9
        
            4
           / \
          7   2
         / \ / \
        6  9 1  3
        
            4
           / \
          7   2
         / \ / \
        9  6 3  1
'''
