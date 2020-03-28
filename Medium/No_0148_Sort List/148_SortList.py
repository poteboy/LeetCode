#Runtime: 300 ms, faster than 14.19% of Python3 online submissions for Sort List.
#Memory Usage: 39.4 MB, less than 15.38% of Python3 online submissions for Sort List.

# 一般的なmerge sortの知識、No21 merge two sorted lists と No876 middle of the linked listのtwo pointer techniueの知識が必要
#それらを駆使してもこれだけ悪い成績なので、かなり難しい。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        l1, l2 = self.divideList(head)
        l1 = self.sortList(l1)
        l2 = self.sortList(l2)
        head = self.mergeLists(l1,l2)
        return head
    
    def mergeLists(self, l1, l2):
        # No21 を参照
        tmp = None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            tmp = l1
            tmp.next = self.mergeLists(l1.next, l2)
        else:
            tmp = l2
            tmp.next = self.mergeLists(l1, l2.next)
        return tmp
    
    def divideList(self, head):
        # two pointer technique を使って真ん中を見つける
        slow = head
        fast = head
        if fast:
            fast = fast.next
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next
        mid = slow.next
        slow.next = None
        return head, mid
            
