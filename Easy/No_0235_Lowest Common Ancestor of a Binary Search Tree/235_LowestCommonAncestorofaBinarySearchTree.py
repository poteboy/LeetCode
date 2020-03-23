
#Runtime: 80 ms, faster than 60.99% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
#Memory Usage: 16.9 MB, less than 100.00% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #片方が＝になったら、それがAncestorだから、return。
        #片方がrootより小さくて、片方が大きかったらそこで分岐してるからreturn
        #それ以外の場合は、奥に進む。
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p , q)
        else:
            return root
        
