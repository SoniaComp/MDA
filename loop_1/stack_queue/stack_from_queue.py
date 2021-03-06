from collections import deque
class MyStack:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        
    # 요소 삽입 후 맨 앞에 두는 상태로 재정렬
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()
        
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]
        
        
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue # 여기서는 len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()