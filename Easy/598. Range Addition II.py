class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m * n
        arr = zip(* ops)
        ans = []

        for each in arr:
            ans.append(min(each))

        return ans[0] * ans[1]
