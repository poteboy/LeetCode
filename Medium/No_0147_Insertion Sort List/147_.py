
#Runtime: 188 ms, faster than 76.76% of Python3 online submissions for Insertion Sort List.
#Memory Usage: 15.9 MB, less than 25.00% of Python3 online submissions for Insertion Sort List.

from __future__ import annotations
class ListNode(object):
    def __init__(self, val:int, next: ListNode = None):
        self.val = val
        self.next = next

node8 = ListNode(4)
node7 = ListNode(2, node8)
node6 = ListNode(7, node7)
node5 = ListNode(8, node6)
node4 = ListNode(1, node5)
node3 = ListNode(3, node4)
node2 = ListNode(5, node3)
node1 = ListNode(6, node2)

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        tmp = ListNode(0)
        tmp.next = insert = head

        while head and head.next:
            if head.val > head.next.val:
                insert = head.next
                insert_pre = tmp
                while insert_pre.next.val < insert.val:
                    insert_pre = insert_pre.next
                head.next = insert.next
                insert.next = insert_pre.next
                insert_pre.next = insert
            else:
                head = head.next
        return self.show(tmp.next)

    def show(self, root):
        ans = []
        while root:
            ans.append(root.val)
            root = root.next
        return ans
        
s = Solution()
print(s.insertionSortList(node1))
