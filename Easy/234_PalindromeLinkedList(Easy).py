
#Linkedlistの全てのnodeのvalをリストに格納し、そのリストを反転させてものが同じか調べる

#Runtime: 64 ms, faster than 89.48% of Python3 online submissions for Palindrome Linked List.
#Memory Usage: 23 MB, less than 100.00% of Python3 online submissions for Palindrome Linked List.

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x:int =None):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        x = head
        nodes = []
        while x:
            nodes.append(x.val)
            x = x.next
        
        nodes_reversed = nodes[::-1] #逆順
        '''
        別のやり方として、
        a = [1,2,2,1]
        for i in range(len(a) // 2):
            a[i],a[-1-i] = a[-1-i],a[i]
        と言う方法がある（恐らくこっちの方が早い？
        '''
        if nodes == nodes_reversed:
            return True
        else:
            return False
        

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
    print(s.isPalindrome(head.next))
