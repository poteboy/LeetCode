#Runtime: 88 ms, faster than 53.34% of Python3 online submissions for Count Complete Tree Nodes.
#Memory Usage: 21.1 MB, less than 17.24% of Python3 online submissions for Count Complete Tree Nodes.

from __future__ import annotations
class TreeNode(object):
    def __init__(self, val: int, left: TreeNode = None, right: TreeNode = None):
        self.val = val 
        self.left = left
        self.right = right 


node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node2 = TreeNode(2, node4, node5)
node3 = TreeNode(3, node6, None)
node1 = TreeNode(1, node2, node3)



class Solution:
    def __init__(self):
        self.num = 0

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return self.num
        if root:
            self.num += 1
            return self.countNodes(root.left) and self.countNodes(root.right)

s= Solution()
print(s.countNodes(node1))
