
#Runtime: 28 ms, faster than 65.08% of Python3 online submissions for Binary Tree Inorder Traversal.
#Memory Usage: 13 MB, less than 90.16% of Python3 online submissions for Binary Tree Inorder Traversal.

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.inorder(root, [])
        
    def inorder(self, root, contain):
        #preorderより少し複雑だがやってることは同じ
        #１番左までいけばそれを格納し、その親を格納。その次右。
        if root:
            self.inorder(root.left, contain)
            contain.append(root.val)
            self.inorder(root.right, contain)
        return contain

'''
4 -> 2 -> 5 -> 1 -> 6 -> 3 -> 7
           1
          / \
         2   3 
        / \ / \
       4  5 6  7

''' 
  
if __name__=='__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7) 

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    s= Solution()
    print(s.inorderTraversal(node1))
