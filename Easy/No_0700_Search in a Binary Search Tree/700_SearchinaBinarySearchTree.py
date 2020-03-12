
#Runtime: 76 ms, faster than 62.10% of Python3 online submissions for Search in a Binary Search Tree.
#Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Search in a Binary Search Tree.

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode: #this function keeps track of node while there's node so no need for recursion
        while root is not None:
            if root.val < val:
                root = root.right
            elif root.val > val:
                root = root.left
            else:
                return root
        else:
            return None
