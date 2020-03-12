
#スタックのLIFOの特性を生かし、同じ値が重なったら２つともpopする

#Runtime: 228 ms, faster than 9.98% of Python3 online submissions for Remove All Adjacent Duplicates In String.
#Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Remove All Adjacent Duplicates In String.

from collections import deque
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = MyStack()
        while S:
            stack.push(S[0])
            S = S[1:]
        return stack.show()
            
class MyStack:
    def __init__(self):
        self.deque = deque()
        
    def push(self, x:str):
        self.deque.append(x)
        if len(self.deque) >= 2:
            if self.deque[-1] == self.deque[-2]:
                self.pop()
                self.pop()
        
    def pop(self):
        return self.deque.pop()
    
    def show(self):
        return ''.join(self.deque)
     
if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates("abbaca"))
