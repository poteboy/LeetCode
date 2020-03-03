
#初・自力で解いたLinkedListの問題。
#Runtime: 72 ms, faster than 46.69% of Python3 online submissions for Remove Linked List Elements.
#Memory Usage: 15.7 MB, less than 100.00% of Python3 online submissions for Remove Linked List Elements.

'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x = None):
        self.val = x
        self.next = None
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while True:
            if head is None:
                return head
            if head.val == val:
                head = head.next
            elif head.next is None:
                return head
            else:
                ptr = head
                while ptr and ptr.next is not None:
                    while ptr.next is not None and ptr.next.val is not val:
                        ptr = ptr.next
                        if ptr is None:
                            return 
                    if ptr.next is not None:
                        ptr.next = ptr.next.next
                    else:
                        ptr.next = None
                return head
        
def content(x): 
    while x is not None:
        print(x.val)
        x = x.next  



if __name__ == '__main__':

    head = ListNode()
    node = head
    while True:
        n = int(input('追加：'))
        if n != -1:
            node.next = ListNode(n)
            node = node.next
        else:
            break
    s = Solution()
    s.removeElements(head, 1)
    content(head)        
 
