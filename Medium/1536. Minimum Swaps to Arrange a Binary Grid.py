class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        l = len(grid)
        b = []
        for r in grid:
            i = l
            while i -1 >= 0 and r[i - 1] == 0:
                i -= 1

            b += l - i,

        ans = 0
        for req in range(l - 1, -1, -1):
            for i, v in enumerate(b):
                if v >= req:
                    ans += i
                    b.pop(i)
                    break
            else:
                return -1

        return ans
