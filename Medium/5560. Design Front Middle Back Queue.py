class FrontMiddleBackQueue:

    def __init__(self):
        self.stack = []

    def pushFront(self, val: int) -> None:
        self.stack = [val] + self.stack

    def pushMiddle(self, val: int) -> None:
        mid = len(self.stack) // 2
        self.stack.insert(mid, val)

    def pushBack(self, val: int) -> None:
        self.stack += val,

    def popFront(self) -> int:
        if not self.stack:
            return -1
        return self.stack.pop(0)

    def popMiddle(self) -> int:
        if not self.stack:
            return -1
        if len(self.stack) & 1:
            return self.stack.pop(len(self.stack) // 2)
        return self.stack.pop(len(self.stack) // 2 - 1)

    def popBack(self) -> int:
        if not self.stack:
            return -1
        return self.stack.pop()
