class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [i for i in range(n - 1)]
        return ans + [-sum(ans)]
