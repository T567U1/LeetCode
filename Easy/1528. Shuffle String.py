class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [0] * len(s)
        for x, y in zip(indices, s):
            ans[x] = y

        return ''.join(ans)
