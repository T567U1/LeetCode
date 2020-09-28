# weird program just ding your own stack fuction.....
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        r = self.stack[-1]
        self.stack.pop()
        return r

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.stack

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(5)
obj.push(6)
print(obj.top())
obj.pop()
print(obj.top(), obj.empty())
obj.pop()
print(obj.empty())
