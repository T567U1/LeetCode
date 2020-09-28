from itertools import permutations as p
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = {}
        for i in range(1, len(tiles) + 1):
            for j in p(tiles, i):
                ans[j] = 0

        return len(ans)
