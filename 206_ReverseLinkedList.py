# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#再帰のやり方もあるがまだ理解できていないので後で復習

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None 
        x= head
        while x is not None:
            temp = x.next
            x.next = prev
            prev = x
            x = temp
        head = prev
        return head
        
