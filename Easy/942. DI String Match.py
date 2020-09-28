class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        n, i, rlist = len(S), 0, []
        for l in S:
            if l is 'I':
                rlist.append(i)
                i += 1
            else:
                rlist.append(n)
                n -= 1
        rlist.append(i)
        return rlist
