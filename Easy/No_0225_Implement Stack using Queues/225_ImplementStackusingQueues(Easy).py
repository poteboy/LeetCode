#dequeを使わない実装は155_MinStackで行っているのでそちらを参照。
#両方で試したがテストケースにおける実行速度の差は無かった。

#Runtime: 28 ms, faster than 56.30% of Python3 online submissions for Implement Stack using Queues.
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Implement Stack using Queues.

from collections import deque
class MyStack:

    def __init__(self, capacity: int = 1000):
        self.deque = deque()
        """
        Initialize your data structure here.
        """


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.deque.append(x)
        

    def pop(self) -> int: 
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.deque.pop() #FIFO(キュー）として使いたければ、popの代わりにpopleftを使う
        
    def top(self) -> int:
        """
        Get the top element.
        """
        return self.deque[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.deque) <= 0
 


if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(stack.top())
    print(stack.pop())
    print(stack.empty())
