class FirstUnique:
    def __init__(self, nums: List[int]):
        self.queue = collections.deque(nums)
        self.count = collections.Counter(nums)
        self.ptr = None
        for i in range(len(self.queue)):
            if self.count[self.queue[i]] == 1:
                self.ptr = i
                break

    def showFirstUnique(self) -> int:
        if self.ptr is not None and self.ptr < len(self.queue):
            return self.queue[self.ptr]
        return -1

    def add(self, value: int) -> None:
        self.count[value] += 1
        self.queue.append(value)
        if self.ptr is None:
            self.ptr = 0
        while self.ptr < len(self.queue) and self.count[self.queue[self.ptr]] > 1:
            self.ptr += 1

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
