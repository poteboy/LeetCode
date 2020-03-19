

Runtime: 28 ms, faster than 66.35% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Binary Tree Preorder Traversal.


from typing import List
#Definition for a binary tree node.
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    '''
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        container = self.preorder(root, '')
        ans = container.split()
        return [int(i) for i in ans]
        
    
    def preorder(self, root: TreeNode, tmp:str) -> str:
        if root:
            tmp += (str(root.val) + ' ')
            tmp = self.preorder(root.left, tmp)
            tmp = self.preorder(root.right, tmp)
        return tmp

        #strで文字列を作ってそれをリスト化してその中をint化してるのでかなり遅い
        #下の解法はそのままリストに格納する方法
    '''
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return self.makeList(root, [])
    
    def makeList(self, root, kakko):
        if root:
            kakko.append(root.val)
            self.makeList(root.left, kakko)
            self.makeList(root.right, kakko)
        return kakko
    
        
'''
      1
     / \
    2   3
   / \  / \
  4   5 6  7
'''

if __name__ =="__main__":
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

    s = Solution()

    #print(s.preorderTraversal(node1))
    print(s.prelist(node1, []))
    

        
