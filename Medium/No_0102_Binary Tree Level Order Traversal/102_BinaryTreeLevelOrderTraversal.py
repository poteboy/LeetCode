#Runtime: 36 ms, faster than 39.67% of Python3 online submissions for Binary Tree Level Order Traversal.
#Memory Usage: 14.1 MB, less than 11.29% of Python3 online submissions for Binary Tree Level Order Traversal.


from __future__ import annotations
class ListNode(object):
    def __init__(self, val:int, left : ListNode =None, right: ListNode = None ):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right]) 
                #同じ階層を丸ごと追加するから、extendで中を守る。
            level = [node for node in temp if node]
        return ans
        
if __name__ == '__main__':
    node4 = ListNode(15)
    node5 = ListNode(7) 
    node2 = ListNode(9)
    node3 = ListNode(20, node4, node5)
    node1 = ListNode(3, node2, node3)
    s = Solution()
    print(s.levelOrder(node1))
