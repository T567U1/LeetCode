from itertools import permutations as p
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        a = p(list(range(1, n + 1)))
        for i, x in enumerate(a):
            if i + 1 == k:
                return ''.join([str(i) for i in x])
