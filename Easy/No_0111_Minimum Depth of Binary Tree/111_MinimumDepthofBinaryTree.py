#先輩の助けがあってできました。
#これからBinary Treeもどんどん解いていこうと思います。

#Runtime: 44 ms, faster than 58.03% of Python3 online submissions for Minimum Depth of Binary Tree.
#Memory Usage: 15.1 MB, less than 62.16% of Python3 online submissions for Minimum Depth of Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def dig(root):
            if root.left is None and root.right is None:
                return 0
            elif root.left is None:
                return dig(root.right) + 1
            elif root.right is None:
                return dig(root.left) + 1
            else:
                left = dig(root.left) + 1
                right = dig(root.right) + 1
                return left if left < right else right
        return dig(root) + 1
                
