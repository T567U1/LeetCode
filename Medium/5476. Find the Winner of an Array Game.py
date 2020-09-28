class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k > len(arr):
            return max(arr)
        t = k
        prev = max(arr[:2])
        for i in arr[1:]:
            if not k:
                return prev
            max_ = max(prev, i)
            if max_ == prev:
                k -= 1
            else:
                k = t - 1
            prev = max_
        else:
            return prev
