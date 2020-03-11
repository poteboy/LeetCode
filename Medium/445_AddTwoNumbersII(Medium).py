

#Runtime: 72 ms, faster than 74.63% of Python3 online submissions for Add Two Numbers II.
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Add Two Numbers II.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
from typing import MutableSequence
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list = self.convert(l1) 
        l2_list = self.convert(l2)
        l1 = int(''.join([str(i) for i in l1_list])) #convert arry to integer 
        l2 = int(''.join([str(i) for i in l2_list]))
        ans = l1 + l2 
        return self.makeList(str(ans))
        
    
    def convert(self, l) -> MutableSequence: #put the value of every node contained in the given LinkedList into an array
        ans = []
        while l:
            ans.append(l.val)
            l = l.next
        return ans
    
    def makeList(self, ans: str) -> ListNode:
        head = ListNode(int(ans[0]))
        node = head
        for s in ans[1:]:
            node.next = ListNode(int(s))
            node = node.next
        return head
