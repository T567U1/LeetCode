class SnapshotArray:
    called = -1
    catch = {}

    def __init__(self, length: int):
        self.dic = {}

    def set(self, index: int, val: int) -> None:
        self.dic[index] = val

    def snap(self) -> int:
        self.called += 1
        self.catch[self.called] = self.dic.copy()
        return self.called

    def get(self, index: int, snap_id: int) -> int:
        if index in self.catch[snap_id]:
            return self.catch[snap_id][index]
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
