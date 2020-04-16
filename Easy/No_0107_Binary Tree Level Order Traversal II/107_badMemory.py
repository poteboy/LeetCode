#Runtime: 32 ms, faster than 74.82% of Python3 online submissions for Binary Tree Level Order Traversal II.
#Memory Usage: 14 MB, less than 7.41% of Python3 online submissions for Binary Tree Level Order Traversal II.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        ans = deque()
        level = [root]
        while level:
            ans.appendleft([node.val for node in level])
            tmp = []
            for node in level:
                tmp.extend([node.left, node.right])
            level = [node for node in tmp if node]
        return ans
        
