class Solution:
    def trimMean(self, arr: List[int]) -> float:
        t = len(arr) * 0.05
        t1 = t2 = t
        print(max(arr))
        while t1:
            arr.remove(max(arr))
            t1 -= 1
        while t2:
            arr.remove(min(arr))
            t2 -= 1
        return sum(arr) / len(arr)
