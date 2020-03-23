#木をinorderでリストに格納した後それをソートした後にキューに格納しているので信じられない程遅い。
#最優先で復習。

#Runtime: 388 ms, faster than 5.37% of Python3 online submissions for Binary Search Tree Iterator.
#Memory Usage: 20.3 MB, less than 7.69% of Python3 online submissions for Binary Search Tree Iterator.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.deque = deque()
        self.root = root
        self.contain = self.inorder(root)
        for i in self.contain:
            self.deque.append(i)
        
    def inorder(self, root):
        container = []
        def packing(root, container):
            if root:
                packing(root.left, container)
                container.append(root.val)
                packing(root.right, container)
            container.sort()
            return container
        return packing(root, container)
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.deque.popleft()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if len(self.deque) >= 1:
            return True
        else:
            return False
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
