from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dct = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dct:
            return -1
        self.dct.move_to_end(key)
        return self.dct[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.dct:
            if len(self.dct) >= self.capacity:
                self.dct.popitem( last = False) # last=True, LIFO; last=False, FIFO
            self.dct[key] = value
        else:
            self.dct.move_to_end(key)
            self.dct[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
