#記念すべきLeetCode50問目に解いた問題！
#Runtime: 40 ms, faster than 79.09% of Python3 online submissions for Odd Even Linked List.
#Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Odd Even Linked List.

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x:int = None):
        self.val = x
        self.next = None

#奇数項のnodeを並べたlinkedlistと偶数項のnodeを並べたlinkedlistをつくり、奇数項の最後のnodeのnextを偶数項の最初のnodeに繋げる

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head is not None and head.next is None:
            return head
        odd = head #奇数を繋げる
        odd_track = odd
        even = head.next #偶数を繋げる（そのためスタートは２項目から）
        even_track = even
        
        while odd: 
            if odd.next is not None and odd.next.next is not None:
                if odd.next != even: #偶数linkedlistの1項目と重なった場合（同じnodeを２項目に持ってきてしまう）
                    even.next = odd.next
                    even = even.next
                odd.next = odd.next.next
                odd = odd.next
                #この条件式が唯一breakしないのでodd.next = even_track（最初と最後を繋げる命令文）はここでは必要なし
            elif odd.next is not None:
                if odd.next != even:
                    even.next = odd.next
                    even = even.next
                odd.next = even_track
                break
            else:
                #ここではoddのnodeにnextが存在しない場合で、その時はevenのnodeもそこで終える必要がある
                # 何故なら、そうしないとevenのlinekedlistの最後のポインターとoddのlinkedlistの最後のポインターが重なってしまう
                #つまりevenリストの最後のnodeが奇数になってしまう
                even.next = None
                even = even.next
                odd.next = even_track
                break
        return odd_track #上でoddとevenのlinekdlistを繋げたので、oddのlinekdlistの最初のnodeにポインターを指すodd_trackを返す。
            
        
        

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
    odd = s.oddEvenList(head.next)
    print(content(odd))
