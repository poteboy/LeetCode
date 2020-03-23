# LinkedListを一度普通の配列に変換してから二分探索をおこなっているので、計算量はO(n log n)となり、少し遅い。


#Runtime: 132 ms, faster than 54.59% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
#Memory Usage: 19.3 MB, less than 53.33% of Python3 online submissions for Convert Sorted List to Binary Search Tree.

from typing import MutableSequence
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None 

head = ListNode(-10)
node1 = head
node2 = ListNode(-3)
node1.next = node2
node3 = ListNode(0)
node2.next = node3
node4 = ListNode(5)
node3.next = node4
node5 = ListNode(9)
node4.next = node5

class Solution:
    def sortedListToBST(self, node:ListNode):
        arr = []
        while node is not None:
            arr.append(node.val)
            node = node.next
        return self.convert(arr)
        
        

    #head = [-10, -3, 0, 5, 9]

    def convert(self, arr: MutableSequence):
        pl = 0
        pr = len(arr) -1
        def toBST(pl,pr):
            if pl > pr:
                return None
            mid = (pl + pr)//2
            node = TreeNode(arr[mid])
            if pl == pr:
                return node
            node.left = toBST(pl, mid-1)
            node.right = toBST(mid+1, pr)
            return node
        return toBST(pl, pr)


if __name__ == '__main__':
    s = Solution()
    print(s.sortedListToBST(head))
