#この問題は、消さなきゃいけないnodeが与えられる。
#そのnodeは一番最後ではないという条件があるので、そのnodeの値を次のnodeの値に書き換え、次のnodeを次の次のnodeにするだけ


#Runtime: 36 ms, faster than 77.69% of Python3 online submissions for Delete Node in a Linked List.
#Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Delete Node in a Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node and node.next:
            node.val = node.next.val 
            node.next = node.next.next
            
