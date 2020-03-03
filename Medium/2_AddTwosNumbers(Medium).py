#Runtime: 80 ms, faster than 19.89% of Python3 online submissions for Add Two Numbers.
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x:int = None):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.convert(l1)
        b = self.convert(l2)
        a = int(''.join(reversed(a)))
        b = int(''.join(reversed(b)))
        ans = [int(i) for i in str(a + b)]

        head = ListNode(0)
        ptr = head
        for i in ans[::-1]:
            newNode = ListNode(i)
            ptr.next = newNode
            ptr = ptr.next
        return head.next

    
    def convert(self, l):
        num = []
        while l:
            tmp = l.val
            tmp = str(tmp)
            num.append(tmp)
            l = l.next
        return num
