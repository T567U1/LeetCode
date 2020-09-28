class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = {}

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.keys:
            self.keys[key] += 1
        else:
            self.keys[key] = 1

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        print(self.keys)
        if key in self.keys and self.keys[key] == 1:
            del self.keys[key]
        elif key in self.keys and self.keys[key] > 1:
            self.keys[key] -= 1
        else:
            return

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.keys:
            return max(self.keys, key = self.keys.get)
        else:
            return ''

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.keys:
            return min(self.keys, key = self.keys.get)
        else:
            return ''

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
