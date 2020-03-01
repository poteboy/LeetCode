#Runtime: 3920 ms, faster than 5.02% of Python3 online submissions for Min Stack.
#Memory Usage: 16.5 MB, less than 91.07% of Python3 online submissions for Min Stack.

#恐らく最初にcap(容量)をかなり多めに設定しているのが遅さの原因だと思われる。
#time complexity of getMin function is O(N) so that may be a part of the problem why it's so slow
#In order to fix this problem it's neccessary to find a O(1) solution.


from typing import Any
class MinStack:
    
    def __init__(self, cap: int = 10000) -> None:
        """
        initialize your data structure here.
        """
        self.stk = [None] * cap
        self.capacity = cap
        self.ptr = 0
    
    def push(self, value: int) -> None:
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> None:
        self.ptr -= 1
        
    def top(self) -> int:
        return self.stk[self.ptr - 1] 

    def getMin(self) -> int:
        min_value = self.stk[0]
        for i in range(self.ptr):
            if self.stk[i] < min_value:
                min_value = self.stk[i]
        return min_value
