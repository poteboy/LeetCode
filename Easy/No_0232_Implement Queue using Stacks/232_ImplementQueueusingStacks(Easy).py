
#Runtime: 28 ms, faster than 56.09% of Python3 online submissions for Implement Queue using Stacks.
#Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Implement Queue using Stacks.

from collections import deque
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.deque = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.deque.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.deque.popleft()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.deque[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.deque) <= 0
        
if __name__ =='__main__':
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek())
    print(queue.pop())
    print(queue.empty())
