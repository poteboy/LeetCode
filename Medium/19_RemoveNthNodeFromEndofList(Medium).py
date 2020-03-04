#Runtime: 28 ms, faster than 83.72% of Python3 online submissions for Remove Nth Node From End of List.
#Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Remove Nth Node From

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x:int = None):
        self.val = x
        self.next = None

class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = head
        num = self.HowManyNode(node) - n 
        if num == 0: #linkedlistの最初の値を消したい場合
            head = head.next
            return head
        num -= 1
        ptr = head
        #ここでptrを代入したのは、headにすると、ポインターが進んでしまうから
        while True: #削除したいnodeに辿りつくまで進む
            if num > 0:
                ptr = ptr.next 
                num -= 1
            elif num <= 0:
                ptr.next = ptr.next.next
                return head

    def HowManyNode(self, node) -> int: #ここでlinkedlistが何個nodeを持っているのか調べる
        num = 0
        while True:
            if node is not None:
                num += 1
                node = node.next
            if node is None:
                break
        return num

def content(x): 
    while x is not None:
        print(x.val)
        x = x.next 

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
    ans = s.removeNthFromEnd(head.next, 2)
    content(ans)
