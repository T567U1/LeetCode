class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ans = [0] * len(queries)
        def f(s):
            sl = list(set(s))
            sl.sort()
            return s.count(sl[0])

        q = list(map(f, queries))
        w = list(map(f, words))

        for i, x in enumerate(q):
            for j in w:
                if x < j:
                    ans[i] += 1

        return ans
