class CustomStack:

    def __init__(self, maxSize: int):
        self._len = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == self._len:
            return
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        i = 0
        while i != k and i < len(self.stack):
            self.stack[i] += val
            i += 1


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
