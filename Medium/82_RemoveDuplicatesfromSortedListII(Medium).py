#Runtime: 48 ms, faster than 13.41% of Python3 online submissions for Remove Duplicates from Sorted List II.
#Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted List II.

#O(nm)のためかなり遅い。要改善。

from typing import MutableSequence
class ListNode:
    def __init__(self, x:int = None):
        self.val = x
        self.next = None
        
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        duplicate = [] #重複した数字を中に入れておく
        x =  head 
        while x and x.next: #最後に残った数字は重複しようがないから、nextが無いときはなにもしない
            if x.val == x.next.val:
                duplicate.append(x.val) #重複した数字をarryに格納する
                x.next = x.next.next
            else:
                x = x.next
            #この段階でheadからは重複は消えているが、重複の元となる数値は残っている
        return self.delete(head, duplicate)
        
    def delete(self, head:ListNode, duplicate:MutableSequence) -> ListNode: 
        x = head
        #もし最初の値を消さなければならなくなった時、連続で重複したときなどの不測に備え、新しいlinkedlistをつくる
        ans = ListNode(0) #正解用のlinkedlist
        tmp = ans
        while True:
            if not x:
                break
            if x.val not in duplicate:#x.valは重複していないから、正解のlinkedlistに送る。
                tmp.next = ListNode(x.val)
                tmp = tmp.next
                x = x.next
            else:
                x = x.next
        return ans.next





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
    ans = s.deleteDuplicates(head.next)
    content(ans)
