
#もっといい方法に、two pointers techniqueというのがある

#Runtime: 24 ms, faster than 85.33% of Python3 online submissions for Middle of the Linked List.
#Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Middle of the Linked List.

from math import ceil
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x:int = None):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        node = head
        num = ceil((self.HowManyNode(node) +1) /2) -1 
        #真ん中が二つある（つまりLinkedlistが2つ)なら大きい方を返す。ceilで切り上げ
        while True:
            if num != 0:
                head = head.next
                num -= 1
            elif num == 0:
                return head.val

    def HowManyNode(self, node) -> int:
        num = 0
        while True:
            if node is not None:
                num += 1
                node = node.next
            if node is None:
                break
        return num


if __name__ == "__main__":
    head = ListNode()
    node = head
    while True:
        n = int(input('Value:'))
        if n != -1:
            node.next = ListNode(n)
            node = node.next
        else:
            break
    s = Solution()
    print(s.middleNode(head.next))
