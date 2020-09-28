class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        m = [i for i in range(1, m + 1)]
        p = []
        for i in queries:
            p.append(m.index(i))
            temp = [m.pop(m.index(i))]
            m = temp + m

        return p
