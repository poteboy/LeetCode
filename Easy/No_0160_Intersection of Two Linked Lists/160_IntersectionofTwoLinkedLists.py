
#Runtime: 160 ms, faster than 86.46% of Python3 online submissions for Intersection of Two Linked Lists.
#Memory Usage: 28.1 MB, less than 100.00% of Python3 online submissions for Intersection of Two Linked Lists.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ptrA, ptrB = headA, headB
        countA, countB = 0, 0 #Coutnt the lengths of both heads
        while ptrA:
            countA += 1
            ptrA = ptrA.next
        while ptrB:
            countB += 1
            ptrB = ptrB.next
        diff = abs(countA - countB) #find the absolute difference of the heads which we need when we want to move the pointer of the shorter head. 
        longer = None
        if countA > countB:
            longer = headA
        else:
            longer = headB
        if longer is headA:
            while diff != 0:
                headA = headA.next
                diff -= 1
        else:
            while diff != 0:
                headB = headB.next
                diff -= 1
        while headA and headB:
            if headA is headB: #valが同じでも同じnodeとは限らない。Don't forget "head" is just a pointer.
                return headA
            else:
                headA = headA.next
                headB = headB.next
        else:
            return None
