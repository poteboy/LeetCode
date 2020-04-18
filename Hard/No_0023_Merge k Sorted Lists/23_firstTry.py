#初見１発クリア。メモリをかなり使っているので、そこを改善。

#Runtime: 96 ms, faster than 91.79% of Python3 online submissions for Merge k Sorted Lists.
#Memory Usage: 18.1 MB, less than 7.57% of Python3 online submissions for Merge k Sorted Lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import List
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ans = []
        for node in lists:
            ans.extend(self.helper(node))
        ans.sort()
        
        return self.createList(ans)
        
        
    def helper(self, node):
        tmp = []
        while node:
            tmp.append(node.val)
            node = node.next
        return tmp
    
    def createList(self, arr: List[int]):
        head = ListNode(0)
        node = head
        for i in arr:
            tmp = ListNode(i)
            node.next =tmp
            node = node.next
        return head.next
        
